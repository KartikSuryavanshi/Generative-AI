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


<img width="484" height="252" alt="Screenshot 2026-01-16 at 2 09 33 PM" src="https://github.com/user-attachments/assets/fc97087f-87d4-4851-b096-902c5342baa3" />



## 🧾 Project 3: Invoice Extractor using Gemini Pro Vision

An **intelligent invoice extraction system** built using **Google’s Gemini Pro Vision (Gemini 1.5 Flash)** and **Streamlit**, capable of extracting structured information from invoice images using **multimodal Generative AI**.

This project demonstrates how **vision + language models** can be used to automate document understanding tasks such as invoice processing.

### 🔑 Key Highlights
- Uses **Gemini Pro Vision (Multimodal LLM)**
- Upload invoice images (PNG, JPG, etc.)
- Extracts invoice details using **prompt-based vision understanding**
- Supports **custom extraction prompts**
- Fast inference using **Gemini 1.5 Flash**
- Clean and interactive **Streamlit UI**
- End-to-end AI-powered document processing workflow


<img width="1141" height="752" alt="Screenshot 2026-01-17 at 11 21 53 AM" src="https://github.com/user-attachments/assets/47fc52e3-5ace-45a8-a67a-6fae9c11691b" />


---

# Generative AI:

<img width="1058" height="560" alt="Screenshot 2026-01-20 at 9 42 40 AM" src="https://github.com/user-attachments/assets/9ae3a0bd-8422-4318-9685-ce9e3278cbe8" />

<img width="1043" height="511" alt="Screenshot 2026-01-20 at 10 03 24 AM" src="https://github.com/user-attachments/assets/b41a12e0-7641-448b-a0af-027c15ff0dfa" />
<img width="1001" height="475" alt="Screenshot 2026-01-20 at 10 04 38 AM" src="https://github.com/user-attachments/assets/4000adef-e82d-4788-b0da-d55f00e78785" />

<img width="1047" height="416" alt="Screenshot 2026-01-20 at 10 05 20 AM" src="https://github.com/user-attachments/assets/f76aa163-d9ee-4f71-bf83-fdc4c5cc7ead" />


<img width="1126" height="509" alt="Screenshot 2026-01-20 at 10 09 01 AM" src="https://github.com/user-attachments/assets/9477df46-5422-41a5-8f6e-068a7a8fed5d" />

<img width="1046" height="611" alt="Screenshot 2026-01-20 at 10 09 40 AM" src="https://github.com/user-attachments/assets/1c04eff9-2eb2-41b6-b454-12b9c7cb5e20" />




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

### 🔹 Hugging Face + LangChain Integration
- Learned how to use **open-source LLMs from Hugging Face** with LangChain
- Running **local Hugging Face models** using `HuggingFacePipeline`
- Understanding **local inference vs hosted inference**
- Learned how to use **Hugging Face Hosted Inference API** via `HuggingFaceEndpoint`
- Running large models **without local GPU dependency**
- Managing **Hugging Face API tokens** securely via environment variables

📓 Notebook:
- `Huggingface-Langchain.ipynb`

---

### 🔹 LlamaIndex (Data Framework for LLMs)
- Understanding **LlamaIndex as a data framework for LLM applications**
- Connecting **custom data sources** to LLMs
- Indexing documents for semantic search
- Querying structured & unstructured data using LLMs
- Comparing **LlamaIndex vs LangChain**
- Using LlamaIndex for **RAG-style workflows**
- Building query engines on top of indexed data

📓 Notebook:
- `test.ipynb`

---

### 🔹 Amazon Bedrock (Managed GenAI Platform)
- Understanding **Amazon Bedrock** as a fully managed GenAI service on AWS
- Accessing **multiple foundation models (FMs)** via a **single API**
- Exploring models from:
  - Anthropic (Claude)
  - AI21 Labs
  - Cohere
  - Meta
  - Stability AI
  - Amazon (Titan models)
- Building **secure, private, and responsible AI applications**
- Using **RAG (Retrieval-Augmented Generation)** with enterprise data
- Private model customization using **fine-tuning**
- Building **AI agents** that interact with enterprise systems & data

---

### 🔹 LLM Fine-Tuning (LoRA, QLoRA & Quantization)
- Understanding **why fine-tuning is needed** vs prompt engineering
- Learning the **end-to-end roadmap for LLM fine-tuning**
- Difference between:
  - Full fine-tuning
  - Parameter-efficient fine-tuning (PEFT)
- Deep intuition behind **LoRA (Low-Rank Adaptation)**
- Understanding **QLoRA** for memory-efficient fine-tuning
- Role of **quantization** in reducing model size & compute cost
- Learning about **1-bit & ultra-low-bit LLMs (1.58-bit models)**
- Exploring how large models can run on limited hardware
- Building **LLMOps pipelines** for training & deployment
- Step-by-step fine-tuning of **LLaMA 2 with custom datasets**
- Fine-tuning **Gemma models** using **LoRA in Keras**
- Understanding trade-offs between:
  - Accuracy
  - Memory
  - Latency
  - Cost

---

## 🛠 Tech Stack Used

### 🔹 Programming & Frameworks
- Python  
- Jupyter Notebook  
- Streamlit  
- Flask  

### 🔹 Large Language Models (LLMs)
- OpenAI (GPT-based models)
- Meta LLaMA 2 (Open-source LLM)
- Google Gemini Pro Vision (Gemini 1.5 Flash)

### 🔹 GenAI Frameworks
- LangChain
- LlamaIndex

### 🔹 Vector Databases
- Pinecone (Serverless)
- ChromaDB  

### 🔹 Embeddings & Retrieval
- OpenAI Embeddings  
- Hugging Face Embeddings  
- Sentence Transformers (`BAAI/bge-large-en-v1.5`)  

### 🔹 Multimodal AI
- Image + Text processing using Gemini Pro Vision
- Vision-based prompt engineering

### 🔹 Tools & APIs
- SerpAPI (Real-time search)
- Wikipedia API
- Hugging Face Hub
- Google Generative AI (Gemini API)

### 🔹 Cloud & Managed GenAI Platforms
- Amazon Bedrock
- AWS (GenAI services & infrastructure)

### 🔹 Document Processing
- PyPDF / PyPDFLoader  
- PDF chunking & ingestion  
- TXT & image-based document handling  

### 🔹 UI & Frontend
- Streamlit
- HTML / CSS (Bootstrap)

### 🔹 Utilities
- dotenv (Environment variable management)
- Pandas
- Logging & callbacks for token/cost tracking

### 🔹 Fine-Tuning & LLMOps
- LoRA (Low-Rank Adaptation)
- QLoRA
- Quantization Techniques
- PEFT (Parameter-Efficient Fine-Tuning)
- LLMOps Pipelines
- Keras (for Gemma fine-tuning)

---

## 🚀 How to Run
1. Clone the repository  
2. Open notebooks in Jupyter Notebook / VS Code  
3. Set environment variables:

   export OPENAI_API_KEY = "your_openai_api_key"
   
   export SERPAPI_API_KEY = "your_serpapi_api_key"
   
   export HUGGINGFACEHUB_API_TOKEN = "your_huggingface_api_token"
   
   export PINECONE_API_KEY = "your_pinecone_api_key"
   
   export PINECONE_INDEX_HOST = "your_pinecone_index_host"

   export GOOGLE_API_KEY = "your_google_api_key"

5. Run the notebook cells sequentially

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Note
This repository reflects my **current progress** and will be **updated daily** as I learn and implement more Generative AI concepts.
