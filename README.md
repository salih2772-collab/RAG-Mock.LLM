# RAG From Scratch (Vendor-Agnostic)

This project implements a complete Retrieval-Augmented Generation (RAG) pipeline from scratch.

## Features
- PDF and TXT ingestion
- Deterministic chunking with overlap
- Pluggable embedding providers (mock)
- In-memory vector store with cosine similarity
- Retrieval-based context injection
- Pluggable LLM providers (mock)
- FastAPI backend

## Architecture
Documents  
→ Chunking  
→ Embeddings  
→ Vector Store  
→ Retrieval  
→ LLM  

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
