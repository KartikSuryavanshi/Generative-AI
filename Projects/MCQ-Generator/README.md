# 📝 MCQ Generator using LangChain & OpenAI

👤 **Author:** Kartik Suryavanshi  

---

## 📌 About the Project

**MCQ Generator** is an end-to-end Generative AI application built using **LangChain** and **OpenAI**, designed to automatically generate **Multiple Choice Questions (MCQs)** from textual content such as **PDF** or **TXT** files.

This project demonstrates how **Large Language Models (LLMs)** can be combined with:
- LangChain chains
- Structured outputs
- Token & cost tracking
- Streamlit UI

to build a **real-world, production-style GenAI application**.

---

## 🚀 Key Features

- Upload **PDF or TXT** files
- Select number of MCQs to generate
- Specify **subject** and **difficulty level**
- Automatic MCQ generation using LLMs
- **Structured JSON output**
- MCQs displayed in **tabular format**
- AI-generated **review/summary**
- **Token usage & cost tracking**
- Interactive **Streamlit web interface**

---

## 🧠 Concepts Used

- Prompt Engineering
- LangChain `PromptTemplate`
- LangChain Chains
- OpenAI Chat Models
- Function-style structured outputs
- Token & cost tracking using callbacks
- Document parsing
- Streamlit UI integration
- Environment variable management

---

## 🛠 Tech Stack

- Python
- OpenAI API
- LangChain
- Streamlit
- Pandas
- PyPDF
- python-dotenv
- AWS EC2 (Ubuntu)

---

## 📂 Important Files

- `StreamlitAPP.py` → Streamlit frontend
- `mcqgenerator.py` → Core MCQ generation logic
- `Response.json` → Structured response schema
- `data.txt` → Sample input text
- `requirements.txt` → Project dependencies
- `setup.py` → Package setup
- `test.py` → Testing & logging
- `experiment/` → Experiments & logs

---

## ☁️ Deployment on AWS EC2 (Ubuntu)

### 1️⃣ Login to AWS
Go to:  
https://aws.amazon.com/console/

### 2️⃣ Create an EC2 Instance
- Search for **EC2**
- Launch an **Ubuntu** instance
- Connect to the instance using SSH

---

### 3️⃣ Update the Server


sudo apt update
sudo apt-get update
sudo apt upgrade -y

###4️⃣ Install System Dependencies

sudo apt install git curl unzip tar make sudo vim wget -y

---

###5️⃣ Clone the Repository

git clone https://github.com/KartikSuryavanshi/MCQ-Generator
ls
cd MCQ-Generator

---

###6️⃣ Create .env File for OpenAI API Key

touch .env
ls -a
vi .env

Inside the editor:

1)Press i (insert mode)

2)Paste your OpenAI API key:OPENAI_API_KEY=your_openai_api_key_here

3)Press ESC

4)Type :wq and press Enter to save & exit

5)Verify:cat .env


---

###7️⃣ Install Python & Pip

sudo apt install python3-pip -y

---

###8️⃣ Install Python Dependencies

pip3 install -r requirements.txt

---

###9️⃣ Run the Streamlit Application

python3 -m streamlit run StreamlitAPP.py

---
🔓 Open Port 8501

In EC2 Security Group:

1)Add Inbound Rule

2)Port: 8501

3)Type: Custom TCP

4)Source: 0.0.0.0/0

5)Now access the app in browser:http://<EC2_PUBLIC_IP>:8501

---

### ⚙️ How to Run Locally

1️⃣ Clone the repository
git clone https://github.com/KartikSuryavanshi/MCQ-Generator.git
cd MCQ-Generator

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables
Create a .env file and add:
OPENAI_API_KEY=your_openai_api_key_here

5️⃣ Run the Streamlit app
streamlit run StreamlitAPP.py








