# Lightweight RAG

A lightweight Retrieval-Augmented Generation (RAG) application built with Python, Streamlit, FAISS, and a local LLM using llama-cpp.

## Features

* Upload PDF documents
* Extract and process text
* Store embeddings in FAISS
* Ask questions about uploaded PDFs
* Local LLM inference using GGUF models
* Streamlit web interface

## Project Structure

```text
lightweight-rag/
├── streamlit_app.py
├── requirements.txt
├── README.md
├── data/
├── models/
└── src/
```

## Installation

```bash
git clone https://github.com/javajisreeja792-ux/lightweight-rag.git
cd lightweight-rag

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
streamlit run streamlit_app.py
```

## Usage

1. Open the Streamlit app.
2. Upload a PDF.
3. Ask questions about the document.
4. Receive answers generated from the document content.

## Author

Sreeja Yadav

