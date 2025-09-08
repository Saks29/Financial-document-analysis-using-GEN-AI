%%writefile app.py

# Built Streamlit app for better user experience

# Importing required libraries
import os
import streamlit as st
from pathlib import Path
from rag import load_and_convert_document, get_markdown_splits, create_or_load_vector_store, build_rag_chain
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from pdf2image import convert_from_path, exceptions
from PIL import Image

# Path to vector DB folder ( Used CONSTANT variable to store the path for best coding practices)
VECTOR_DB_FOLDER = "vector_db"
os.makedirs(VECTOR_DB_FOLDER, exist_ok=True) # Create folder if it doesn't exist

# Function to display PDF content as images in the sidebar
def display_pdf_in_sidebar(pdf_path, file_name):
    '''
    This function converts the PDF to images and displays them in the sidebar.
    I have added Exception handling to catch errors while loading the PDF.
    '''
    try:
        images_folder = Path(VECTOR_DB_FOLDER) / file_name / "images"
        os.makedirs(images_folder, exist_ok=True)

        # Check if images already exist
        image_paths = sorted(list(images_folder.glob("*.png"))) # Sort to maintain page order
        if image_paths:
            # If images exist, display them
            for i, img_path in enumerate(image_paths):
                image = Image.open(img_path)
                st.sidebar.image(image, caption=f"Page {i + 1}", use_container_width=True)
        else:
            # Convert PDF to images (one per page)
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                img_path = images_folder / f"page_{i + 1}.png"
                image.save(img_path, "PNG")  # Save image to disk
                st.sidebar.image(image, caption=f"Page {i + 1}", use_container_width=True)

    except exceptions.PDFPageCountError:
        st.sidebar.error("Error: Unable to get page count. The PDF may be corrupted or empty.")
    except exceptions.PDFSyntaxError:
        st.sidebar.error("Error: PDF syntax is invalid or the document is corrupted.")
    except Exception as e:
        st.sidebar.error(f"Error loading PDF: {str(e)}")

# Streamlit title
st.title("📊 DOCUMENT ANALYZER & ASSITANT")

# Subtitle
st.subheader("Use this app to analyze documents and get answer to your questions.\n 💼Its completely Offline ,Secure, Local AI for Your Financial PDFs. Your documents are safe with me! 🤫 ")

# Added Instructions for the user in the sidebar on how how to use the app
with st.sidebar:
    st.markdown("### ℹ️ How to use")
    st.markdown("1. Upload a Document as PDF\n2. Process it\n3. Ask your question ✅")

# Dropdown to select vector DB or upload a new document
vector_db_options = [f.stem for f in Path(VECTOR_DB_FOLDER).glob("*.faiss")]
vector_db_options.append("Upload New Document")
selected_vector_db = st.selectbox("Select existing document or Upload New Document", vector_db_options, index=len(vector_db_options)-1)

# Initialize vector_store to avoid errors
vector_store = None

# If 'Upload New Document' is selected, show the file uploader
if selected_vector_db == "Upload New Document":
    uploaded_file = st.file_uploader("Upload a PDF file for analysis", type=["pdf"])

    # Process the uploaded PDF
    if uploaded_file:
        st.sidebar.subheader("Uploaded PDF")
        st.sidebar.write(uploaded_file.name)

        # Save the PDF file temporarily and display it
        temp_path = f"temp_{uploaded_file.name}"
        document_binary = uploaded_file.read()
        with open(temp_path, "wb") as f:
            f.write(document_binary)

        # Display PDF in the sidebar
        display_pdf_in_sidebar(temp_path, uploaded_file.name.split('.')[0])

        # PDF processing button
        if st.button("Process PDF and Store in Vector DataBase"):
            with st.spinner("Processing document... would be back as it will take a moment :) "):
                markdown_content = load_and_convert_document(temp_path)
                chunks = get_markdown_splits(markdown_content)
                embeddings = OllamaEmbeddings(model='nomic-embed-text', base_url="http://localhost:11434")
                vector_store = create_or_load_vector_store(uploaded_file.name.split(".")[0], chunks, embeddings)
                vector_db_path = Path(VECTOR_DB_FOLDER) / f"{uploaded_file.name.split('.')[0]}.faiss"
                vector_store.save_local(str(vector_db_path))
                
                # Store the actual PDF file for later display
                pdf_path = Path(VECTOR_DB_FOLDER) / f"{uploaded_file.name.split('.')[0]}.pdf"
                with open(pdf_path, "wb") as f:
                    f.write(document_binary)

                st.success("PDF processed and stored! Let me know what questions you need to ask!")
                # Clean up the temporary file
                Path(temp_path).unlink()

elif selected_vector_db != "Upload New Document":
    # Load the selected vector DB
    vector_db_path = Path(VECTOR_DB_FOLDER) / f"{selected_vector_db}.faiss"
    if vector_db_path.exists():
        embeddings = OllamaEmbeddings(model='nomic-embed-text', base_url="http://localhost:11434")
        vector_store = FAISS.load_local(str(vector_db_path), embeddings=embeddings, allow_dangerous_deserialization=True)

        # Display PDF in the sidebar
        pdf_path = Path(VECTOR_DB_FOLDER) / f"{selected_vector_db}.pdf"
        if pdf_path.exists():
            display_pdf_in_sidebar(str(pdf_path), selected_vector_db)
        else:
            st.sidebar.warning("PDF file not found for the selected vector DB.")
    else:
        st.sidebar.warning(f"Vector DB '{selected_vector_db}' not found.")

# Question input section
question = st.text_input("Enter your question:", placeholder="e.g., What is the company's revenue for the quarter?")

# Button to process and generate answers
if st.button("Submit Question") and question:
    if vector_store:
        with st.spinner("Answering your question..."):
            retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k': 5})
            rag_chain = build_rag_chain(retriever)
            response_placeholder = st.empty()
            response = ""
            for chunk in rag_chain.stream(question):
                response += chunk
                response_placeholder.markdown(response.replace('$', '\\$'))
    else:
        st.error("Please upload and process a new document or select a valid existing one first.")


# Added footer
st.markdown("---")
st.markdown("Developed by Saksham Patwal | Powered by LangChain + Ollama | GEN-AI ", unsafe_allow_html=True)
st.markdown("Dont forget to appreciate if it fascinates you and connect & follow")
st.markdown("🧑‍💻[GitHub](https://github.com/Saks29) | 🔗[LinkedIn](https://www.linkedin.com/in/sakpat/)")
