import json
from pathlib import Path
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.utils import read_file, get_table_data

# Load environment variables for OpenAI
load_dotenv()

# Load the response template JSON safely from the repo
TEMPLATE_PATH = Path(__file__).parent / "Response.json"
with open(TEMPLATE_PATH, "r") as f:
    RESPONSE_JSON = json.load(f)

# Streamlit page setup
st.set_page_config(page_title="MCQ Generator", page_icon="🧠", layout="centered")
st.title("MCQs Creator Application 🧠")
st.caption("Generate multiple-choice questions from your content.")

# Input form
with st.form("mcq_form"):
    uploaded_file = st.file_uploader("Upload a text file (txt, pdf)", type=["txt", "pdf"])
    input_text = st.text_area("Or paste text", height=200)
    mcq_count = st.number_input("No. of MCQs", min_value=1, max_value=50, value=5)
    subject = st.text_input("Subject", value="General Knowledge")
    tone = st.selectbox("Tone", options=["neutral", "simple", "formal", "fun"], index=0)
    submit = st.form_submit_button("Create MCQs")

if submit:
    try:
        # Prefer uploaded file; otherwise use pasted text
        if uploaded_file is not None:
            text = read_file(uploaded_file)
        else:
            text = input_text

        if not text or not text.strip():
            st.warning("Please provide source text via upload or paste.")
        else:
            payload = {
                "text": text,
                "number": str(mcq_count),
                "subject": subject.strip() or "General Knowledge",
                "tone": tone,
                "response_json": json.dumps(RESPONSE_JSON),
            }

            with st.spinner("Generating MCQs..."):
                result = generate_evaluate_chain.invoke(payload)

            # Display quiz
            st.subheader("Quiz")
            quiz_text = result.get("quiz")
            if isinstance(quiz_text, str):
                table_data = get_table_data(quiz_text)
                if table_data:
                    df = pd.DataFrame(table_data)
                    df.index = df.index + 1
                    st.table(df)
                else:
                    st.code(quiz_text, language="json")
            else:
                st.write(quiz_text)

            # Display review
            st.subheader("Review")
            st.text_area("Review feedback", value=result.get("review", ""), height=200)

    except Exception as e:
        st.error("An error occurred while generating MCQs.")
        st.exception(e)
