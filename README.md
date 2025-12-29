# 🤖 Generative AI – Hands-On Learning

## 👤 Author
Kartik Suryavanshi  

---

## 📌 About This Repository
This repository contains my **hands-on learning and experimentation with Generative AI**, implemented using **Python and Jupyter Notebooks**.

The work focuses on:
- Interacting with **Large Language Models (LLMs)** via the OpenAI API
- Using **LangChain** for prompt management, chains, agents, tools, and document loaders
- Building practical GenAI workflows instead of just theory

This repository is updated **incrementally as new concepts are learned and implemented**.

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
- Batch processing multiple inputs using function calling
- Tool-style workflows where LLM selects function arguments

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Advanced Function Calling & Tool Execution
- Designing function descriptions for external tools
- Letting the LLM decide which function to call
- Executing Python functions based on LLM output
- Sending tool execution results back to the LLM
- Generating final natural language responses using tool outputs

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
- Improving prompt consistency for production-style workflows

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 LangChain Agents & Tools
- Understanding agent-based reasoning
- Using **ZERO_SHOT_REACT_DESCRIPTION** agent type
- Integrating external tools using LangChain
- Using **SerpAPI** for real-time Google search
- Using **Wikipedia tool** for factual lookups
- Answering real-time and current-affairs questions using tools

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 LangChain Chains
- Understanding the concept of chains
- Using **LLMChain** for single-step workflows
- Using **SimpleSequentialChain** for multi-step pipelines
- Using **SequentialChain** with multiple inputs and outputs
- Passing outputs of one chain as inputs to another
- Building end-to-end reasoning pipelines

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Document Loaders
- Loading PDF documents using **PyPDFLoader**
- Splitting documents into pages
- Preparing documents for downstream GenAI tasks
- Understanding how document loaders fit into RAG-style workflows

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

## 🛠 Tech Stack Used
- Python
- Jupyter Notebook
- OpenAI API
- LangChain
- SerpAPI
- Wikipedia API
- PyPDF

---

## 🚀 How to Run
1. Clone the repository
2. Open the notebooks in Jupyter Notebook or VS Code
3. Set your API keys as environment variables:
export OPENAI_API_KEY="your_openai_api_key"
export SERPAPI_API_KEY="your_serpapi_api_key"
4. Run the notebook cells sequentially

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Note
This repository reflects my **current progress** and will be **updated daily** as I learn and implement more Generative AI concepts.
