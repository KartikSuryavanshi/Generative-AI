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
