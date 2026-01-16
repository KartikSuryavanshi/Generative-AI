# 🤖 Generative AI – Hands-On Learning

## 👤 Author
**Kartik Suryavanshi**

---

## 📌 About This Repository
This repository documents my **hands-on learning journey in Generative AI**, implemented using **Python and Jupyter Notebooks**.

The focus is on **practical implementation rather than theory**.  
All concepts are learned by writing **real production-style code**, experimenting with **LLMs, tools, agents, chains, and frameworks** commonly used in real-world Generative AI systems.

This repository is **continuously updated** as I learn new concepts and build projects.

---

## 🚀 Projects Built Using This Learning

## 🧠 Project 1: MCQ Generator (LangChain + OpenAI)
Alongside notebooks, I have built a **complete end-to-end project** using the concepts learned in this repository.

**Project Name:** MCQ Generator  
**Tech Used:** LangChain, OpenAI API, Streamlit, Python  

**Key Highlights:**
- Generates **MCQs from uploaded PDF/TXT content**
- Uses **LangChain chains and prompt templates**
- Structured JSON output using **LLM-controlled schemas**
- Tracks **token usage and API cost**
- Interactive **Streamlit UI**
- Modular production-style codebase

📌 Repository:
👉 https://github.com/KartikSuryavanshi/MCQ-Generator

<img width="701" height="770" alt="Screenshot 2026-01-07 at 11 15 21 AM" src="https://github.com/user-attachments/assets/7877c756-ffa7-47d6-943c-c91fa53f5db4" />



## 🏥 Project 2: End-to-End Medical Chatbot using LLaMA 2

An **intelligent medical chatbot** powered by **Meta’s LLaMA 2**, **LangChain**, and **Pinecone Vector Database**.

The chatbot provides **context-aware medical responses** based on **uploaded PDF documents**, using a **Retrieval-Augmented Generation (RAG)** architecture.

### 🔑 Key Highlights
- Uses **open-source LLaMA 2** (no OpenAI dependency)
- PDF-based **medical knowledge ingestion**
- Vector search using **Pinecone Serverless**
- Semantic retrieval with embeddings
- RAG-based answer generation
- Modern **Flask + Bootstrap UI**
- Fully production-ready architecture

📌 Repository  
👉 https://github.com/KartikSuryavanshi/Medical-Chatbot

<img width="484" height="252" alt="Screenshot 2026-01-16 at 2 09 33 PM" src="https://github.com/user-attachments/assets/fc97087f-87d4-4851-b096-902c5342baa3" />
---


# Open LLMs:
https://github.com/eugeneyan/open-llms

---

## ✅ What’s Done So Far

### 🔹 OpenAI API Fundamentals
- OpenAI API setup and authentication  
- Listing available OpenAI models  
- Chat-based text generation  
- Understanding request–response flow  
- Prompt experimentation  
- Playground concepts (temperature, max tokens, top-p, penalties)

📓 Notebook:
- `testopenaiapi.ipynb`

---

### 🔹 Structured Output & Function Calling
- Extracting structured JSON data from unstructured text  
- Parsing model responses into Python dictionaries  
- Defining function schemas  
- Enforcing structured outputs using OpenAI function calling  
- Batch processing multiple inputs  
- Tool-style workflows where LLM selects function arguments  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Advanced Function Calling & Tool Execution
- Designing function descriptions for external tools  
- Letting the LLM decide which function to call  
- Executing Python functions based on LLM output  
- Sending tool execution results back to the LLM  
- Generating final natural language responses  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 LangChain Core Concepts
- Using LangChain’s OpenAI LLM wrapper  
- Zero-shot prompting using LangChain  
- Understanding limitations of static LLM knowledge  
- Comparing direct OpenAI API usage vs LangChain abstraction  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Prompt Templates
- Creating reusable prompt templates  
- Dynamic prompt formatting using variables  
- Reducing prompt duplication  
- Improving prompt consistency for production workflows  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 LangChain Agents & Tools
- Understanding agent-based reasoning  
- Using `ZERO_SHOT_REACT_DESCRIPTION` agent  
- Integrating external tools with LangChain  
- Real-time Google search using **SerpAPI**  
- Factual lookups using **Wikipedia tool**  
- Answering real-time/current-affairs questions  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 LangChain Chains
- Understanding chains  
- `LLMChain` for single-step workflows  
- `SimpleSequentialChain` for pipelines  
- `SequentialChain` with multiple inputs/outputs  
- Passing outputs between chains  
- End-to-end reasoning pipelines  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Document Loaders
- Loading PDFs using `PyPDFLoader`  
- Splitting documents into pages  
- Preparing documents for downstream GenAI tasks  
- Understanding RAG-style workflows  

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Memory in LangChain
- ConversationBufferMemory  
- ConversationBufferWindowMemory  
- ConversationChain  
- Context-aware chatbot behavior  

📓 Notebook:
- `langchain.ipynb`

---

### 🔹 Hugging Face Models
- Using open-source models via Hugging Face Hub  
- Running models without OpenAI dependency  
- `google/flan-t5-large`  
- Comparing closed-source vs open-source LLMs  
- Understanding model limitations  

📓 Notebook:
- `LangChain_Course+_Complete.ipynb`

---

### 🔹 Vector Databases

**Concepts Covered:**
- What embeddings are and why they are needed  
- Word embeddings, image embeddings, and multimodal embeddings  
- Converting **data → vector representations** using models  
- How semantic similarity works in vector space  
- Storing embeddings inside **vector databases**  
- Vector similarity search (cosine similarity, dot product, Euclidean distance)  
- End-to-end flow:  
  **Data → Embeddings → Vector Database → Query → Relevant Results**
- Real-world applications:
  - Retrieval-Augmented Generation (RAG)
  - Semantic search
  - Recommendation systems
  - Chatbots with memory

 📄 **Detailed Explanation PDF (Added to Repository):**
- `Vector_Databases_and_Embeddings_Explained.pdf`

---

### 🔹 Embeddings (Text, Words, Objects)
- Understanding embeddings as numerical vector representations  
- Converting:
  - Text → Vector  
  - Words → Vector  
  - Documents → Vector  
- Full pipeline learned:
  Data → Embeddings → Vector Database

---

### 🔹 Pinecone (Managed Vector Database)

- Creating a Pinecone index
- Choosing vector dimensions and similarity metrics
- Storing embeddings inside Pinecone
- Performing similarity search queries
- Integrating Pinecone with LLM-based workflows
- Understanding how Pinecone fits into **RAG architectures**
- Scaling vector search for large datasets

📓 Notebook:
- `Pineconevectordb.ipynb`

This notebook demonstrates **hands-on usage of Pinecone** for real-world vector search scenarios.

---

### 🔹 ChromaDB (Local Vector Database)
- Using ChromaDB for local vector storage  
- Storing document embeddings  
- Performing similarity search  
- Integrating ChromaDB with LangChain retrievers  

📓 Notebook:
- `chromadb.ipynb`

---

### 🔹 Retrieval-Augmented Generation (RAG)
- End-to-end RAG architecture  
- Flow:
  Documents → Embeddings → Vector DB → Retriever → LLM → Answer  
- LLM answers using retrieved context instead of memorization  

📄 Diagram:
- RAG architecture using ChromaDB & OpenAI (PDF)

---

### 🔹 LLaMA 2 with LangChain
- Running **open-source LLMs locally**
- Using LLaMA-2 with LangChain
- Understanding hardware & memory constraints
- Difference between closed-source (OpenAI) vs open-source models

📓 Notebooks:
- `How_to_run_Llama_2.ipynb`
- `Llama_2_LangChain.ipynb`

---

## 🛠 Tech Stack Used
- Python  
- Jupyter Notebook  
- OpenAI API  
- LangChain
- Vector Embeddings
- Pinecone Vector Database
- ChromaDB Vector Database
- Hugging Face Models 
- SerpAPI  
- Wikipedia API  
- PyPDF  
- Streamlit
- Vector Embeddings
- dotenv
- Pandas

---

## 🚀 How to Run
1. Clone the repository  
2. Open notebooks in Jupyter Notebook / VS Code  
3. Set environment variables:

   export OPENAI_API_KEY="your_openai_api_key"
   
   export SERPAPI_API_KEY="your_serpapi_api_key"
   
   export HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"
   
   export PINECONE_API_KEY = "your_pinecone_api_key"
   
   export PINECONE_INDEX_HOST = "your_pinecone_index_host"  

4. Run the notebook cells sequentially

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Note
This repository reflects my **current progress** and will be **updated daily** as I learn and implement more Generative AI concepts.
