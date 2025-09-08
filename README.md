# 📊 Document Analyzer & Assistant |🧾⚡GEN-AI using RAG+LangChain

<div align="center">

<img width="1882" height="819" alt="Screenshot 2025-09-09 011433" src="https://github.com/user-attachments/assets/b0d65699-d5ec-4990-86cb-a1b2de489693" />

**🛡️ Privacy-First • 🤖 AI-Powered • 💻 Completely Offline**

<img width="1853" height="824" alt="Screenshot 2025-09-09 011703" src="https://github.com/user-attachments/assets/6e1f652c-b26f-47ca-8be8-ae0fe7e92de9" />
<img width="1889" height="822" alt="Screenshot 2025-09-09 012132" src="https://github.com/user-attachments/assets/3d0b4773-ab6d-4060-bef2-062aba182e0e" />
<img width="1898" height="830" alt="Screenshot 2025-09-09 012221" src="https://github.com/user-attachments/assets/89eb628d-5c40-4d08-8641-d48b1f70c87e" />

*Transform your document analysis workflow with AI-powered insights while keeping your data completely secure and offline.*

[🚀 Quick Start](#quick-start) • [📖 Documentation](#features) • [🎯 Use Cases](#use-cases) • [🤝 Contributing](#contributing)

</div>

---

## 🌟 Why This Project?

In today's data-driven world, document analysis is crucial, but **privacy shouldn't be compromised**. This tool provides enterprise-grade document intelligence while ensuring your sensitive files never leave your local machine.

### 🎯 Perfect For:
- 💼 **Financial Professionals** - Analyze reports, statements, and financial documents
- 🎓 **Researchers & Students** - Extract insights from academic papers and studies  
- 👥 **HR Teams** - Screen resumes and candidate profiles intelligently
- ⚖️ **Legal Professionals** - Review contracts and legal documents
- 🏢 **Business Analysts** - Process corporate documents and presentations

---

## ✨ Features

### 🔒 **Privacy-First Architecture**
- **100% Offline Processing** - Your documents never leave your machine
- **Local AI Models** - Powered by Ollama for complete data control
- **Secure Vector Storage** - Documents processed and stored locally

### 🧠 **Intelligent Analysis**
- **Natural Language Queries** - Ask questions in plain English
- **Contextual Understanding** - AI comprehends document context and nuances
- **Multi-format Support** - PDF documents up to 200MB
- **Semantic Search** - Advanced vector-based document retrieval

### ⚡ **Performance & Usability**
- **Fast Processing** - Quick document ingestion and analysis
- **Interactive Interface** - Clean, intuitive web-based UI
- **Real-time Responses** - Instant answers to your queries
- **Session Memory** - Maintains conversation context

---

## 🖥️ Screenshots

<div align="center">

### Document Upload Interface
![Upload Interface](https://via.placeholder.com/600x300/2d3748/ffffff?text=Clean+Upload+Interface)

### AI-Powered Analysis
![Analysis Demo](https://via.placeholder.com/600x300/2d3748/ffffff?text=Intelligent+Document+Analysis)

### Question-Answer Interface  
![Q&A Interface](https://via.placeholder.com/600x300/2d3748/ffffff?text=Natural+Language+Q%26A)

</div>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 4GB+ RAM (recommended for optimal performance)
- Ollama installed locally

## 📋 Usage

### Step 1: Upload Document
- Drag and drop your PDF file (max 200MB)
- Wait for processing completion

### Step 2: Ask Questions
- Type natural language questions about your document
- Examples:
  - *"What is the main conclusion of this research?"*
  - *"Which job roles match my skills from this resume?"*
  - *"What are the key financial metrics mentioned?"*

### Step 3: Get Intelligent Answers
- Receive contextual, accurate responses
- Ask follow-up questions for deeper analysis

---

## 🎯 Use Cases

### Resume Analysis
```
Question: "Which IT job role is best suited for me?"
Answer: Based on your B.Tech in Information Technology, 8.38 CGPA, 
and expertise in data science, analytics, and machine learning, 
you're well-suited for roles like Data Scientist, Business 
Intelligence Analyst, or AI-related positions.
```

### Financial Document Review
```
Question: "What is the company's revenue growth trend?"
Answer: [Analyzes financial statements and provides insights 
on revenue patterns, growth rates, and key performance indicators]
```

### Research Paper Analysis
```
Question: "What are the main research methodologies used?"
Answer: [Identifies and explains research methods, sample sizes, 
and analytical approaches used in the study]
```

---

## 🛠️ Technical Architecture

```mermaid
graph LR
    A[PDF Upload] --> B[Document Processing]
    B --> C[Text Extraction]
    C --> D[Chunking & Embedding]
    D --> E[Vector Database Storage]
    E --> F[User Query]
    F --> G[Semantic Search]
    G --> H[Context Retrieval]
    H --> I[AI Response Generation]
    I --> J[Natural Language Answer]
```

### Tech Stack
- **Frontend**: Streamlit (Interactive Web Interface)
- **Backend**: Python, LangChain (Document Processing & AI Orchestration)
- **AI Engine**: Ollama (Local LLM Hosting)
- **Vector DB**: ChromaDB/FAISS (Semantic Search)
- **Document Processing**: PyPDF2, LangChain Document Loaders

---

## 📁 Project Structure

```
document-analyzer-assistant/
├── app.py                 # Main Streamlit application
├── src/
│   ├── document_processor.py  # PDF processing logic
│   ├── vector_store.py        # Vector database operations
│   ├── ai_assistant.py        # AI query processing
│   └── utils.py              # Utility functions
├── requirements.txt       # Python dependencies
├── config/
│   └── settings.py       # Configuration settings
├── data/                 # Local document storage (gitignored)
├── tests/               # Unit tests
├── docs/                # Documentation
└── README.md
```

---

## ⚙️ Configuration & Customization

### Environment Setup
```bash
# .env file configuration
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama2                    # Options: llama2, mistral, codellama
VECTOR_DB_PATH=./data/vectordb
MAX_FILE_SIZE=200                    # Maximum file size in MB
CHUNK_SIZE=1000                      # Text chunk size for processing
CHUNK_OVERLAP=200                    # Overlap between chunks
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Model Recommendations

| Model | Use Case | Speed | Accuracy | RAM Required |
|-------|----------|-------|----------|--------------|
| `llama2:7b` | General documents | ⭐⭐⭐ | ⭐⭐⭐⭐ | 8GB |
| `mistral:7b` | Fast processing | ⭐⭐⭐⭐ | ⭐⭐⭐ | 6GB |
| `codellama:7b` | Technical docs | ⭐⭐ | ⭐⭐⭐⭐⭐ | 8GB |
| `phi:2.7b` | Resource-constrained | ⭐⭐⭐⭐⭐ | ⭐⭐ | 4GB |

### Performance Optimization
- **Batch Processing**: Process multiple documents simultaneously
- **Caching**: Store embeddings for faster re-querying
- **Memory Management**: Automatic cleanup of unused vectors
- **GPU Acceleration**: Optional CUDA support for faster processing

---

## 🤝 Contributing

I welcome contributions! 

### Ways to Contribute:
- 🐛 **Bug Reports** - Help us identify and fix issues
- ✨ **Feature Requests** - Suggest new capabilities
- 📝 **Documentation** - Improve guides and examples
- 🧪 **Testing** - Add test cases and improve coverage
- 💻 **Code** - Submit pull requests for enhancements
