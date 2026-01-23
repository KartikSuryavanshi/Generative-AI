# 📚 RAG-based Information Retrieval System (Video → Knowledge)

## 👤 Author
Kartik Suryavanshi  

---

## 📌 Project Overview
This project implements a **Retrieval-Augmented Generation (RAG) system** using **Ollama** to extract, process, and retrieve relevant information from **video content**.

Videos are converted into audio, transcribed into text, chunked into semantically meaningful segments, embedded into vector representations, and queried using a RAG-based retrieval pipeline.

---

## 🧠 Core Concepts
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Embeddings
- Semantic Chunking
- Similarity Search
- Local LLM Inference with Ollama

---

## 🔄 System Workflow

1. Video Input
2. Audio Extraction
3. Speech-to-Text Conversion
4. Text Chunking
5. Embedding Generation
6. Vector Storage
7. Query Processing
8. Context-Aware Answer Generation

---

## 🛠 Technologies Used

### Generative AI
- Ollama

### Programming Language
- Python

### Data Handling
- JSON-based storage

---

## 📂 Project Structure

RAG-based-Project/
│
├── jsons/
│
├── process_video.py
├── create_chunks.py
├── process_incoming.py
├── read_chunks.py
│
├── output.json
├── README.md


---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9+
- Ollama installed and running locally

---

### 
1)Install Dependencies
pip install -r requirements.txt

2)Process Video Files
python process_video.py

3)Create Text Chunks
python create_chunks.py

4)Generate Embeddings
python process_incoming.py

5)Query the RAG System
python read_chunks.py

---
