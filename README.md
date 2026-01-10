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

### 🧠 MCQ Generator (LangChain + OpenAI)
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


This project demonstrates how notebook-level concepts scale into a **real GenAI application**.

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

### 🔹 Vector Databases & Embeddings

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

## 🛠 Tech Stack Used
- Python  
- Jupyter Notebook  
- OpenAI API  
- LangChain  
- Hugging Face Hub  
- SerpAPI  
- Wikipedia API  
- PyPDF  
- Streamlit
- Vector Embeddings/ Databases

---

## 🚀 How to Run
1. Clone the repository  
2. Open notebooks in Jupyter Notebook / VS Code  
3. Set environment variables:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export SERPAPI_API_KEY="your_serpapi_api_key"
   export HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"

5. Run the notebook cells sequentially

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Note
This repository reflects my **current progress** and will be **updated daily** as I learn and implement more Generative AI concepts.
