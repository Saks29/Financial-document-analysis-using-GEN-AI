# 1. Install poppler-utils, a system dependency for pdf2image
!apt-get update
!apt-get install -y poppler-utils

# 2. Install required Python packages
!pip install -q streamlit langchain langchain_community langchain_ollama \
                 faiss-cpu pypdf pdf2image Pillow docling \
                 langchain_text_splitters pyngrok
                 
print("✅ All dependencies installed.")
