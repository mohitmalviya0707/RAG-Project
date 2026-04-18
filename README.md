# 📚 PDF RAG System - Document Q&A Pipeline

A complete Retrieval-Augmented Generation (RAG) system that loads PDF documents, splits them into chunks, creates embeddings, and stores them in a vector database for semantic search and retrieval.

## ✨ Features

- **PDF Loading**: Extract text from any PDF document using PyPDFLoader
- **Intelligent Chunking**: Recursive text splitting with configurable chunk size and overlap
- **Vector Embeddings**: OpenAI embeddings for semantic understanding
- **Vector Storage**: Persistent Chroma database for efficient similarity search
- **Retrieval Ready**: Built-in retriever interface for RAG applications

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Document Loader | PyPDFLoader (langchain-community) |
| Text Splitter | RecursiveCharacterTextSplitter |
| Embeddings | OpenAIEmbeddings |
| Vector Store | Chroma |
| Framework | LangChain |

## 📋 Prerequisites

- Python 3.9+
- OpenAI API key

## 🚀 Installation

### 1. Install Dependencies

```bash
pip install langchain langchain-community langchain-openai pypdf chromadb python-dotenv tiktoken
