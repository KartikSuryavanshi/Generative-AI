# 🤖 Generative AI – Hands-On Learning

## 👤 Author
Kartik Suryavanshi  
---

## 📌 About This Repository
This repository contains my **hands-on practice while learning Generative AI**, focusing on **practical implementation using Python and Jupyter Notebooks**.

The work here demonstrates **direct interaction with Large Language Models (LLMs)** using the **OpenAI API**, along with **LangChain integration** for prompt management and abstraction.

This repository will be **updated incrementally** as I continue learning.

---

## ✅ What’s Done So Far

### 🔹 OpenAI API Basics
- OpenAI API setup and authentication
- Listing available OpenAI models
- Basic text generation using chat-based models
- Understanding request–response flow
- Prompt experimentation
- Playground concepts (temperature, tokens, penalties)

📓 Notebook:
- `testopenaiapi.ipynb`

---

### 🔹 Structured Output & Function Calling
- Extracting structured JSON data from unstructured text
- Converting model responses into Python dictionaries
- Defining function schemas for structured outputs
- Using OpenAI **function calling** to enforce output format
- Batch processing multiple inputs using function calling
- Tool-style integration where LLM selects function arguments

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 Advanced Function Calling (Tool Integration)
- Designing function descriptions for external tools
- Letting the LLM decide which function to call
- Executing Python functions based on LLM output
- Sending tool results back to the LLM for final responses

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

### 🔹 LangChain Basics
- Using LangChain’s OpenAI LLM wrapper
- Zero-shot prompting
- Comparing direct OpenAI API usage vs LangChain abstraction
- PromptTemplates for reusable and dynamic prompts

📓 Notebook:
- `testopenaiapi_and_langchain.ipynb`

---

## 🛠 Tech Stack Used
- Python
- Jupyter Notebook
- OpenAI API
- LangChain
---

## 🚀 How to Run
1. Clone the repository
2. Open the notebooks in Jupyter Notebook or VS Code
3. Set your OpenAI API key as an environment variable:
export OPENAI_API_KEY="your_api_key_here"
4. Run the notebook cells sequentially

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Note
This repository reflects my **current progress** and will be **updated daily** as I learn and implement more Generative AI concepts.
