from dotenv import load_dotenv
load_dotenv() ## load all environment variables from .env file
import os
import streamlit as st
import sqlite3
import google.generativeai as genai

##configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load google gemini model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content([prompt[0],question])
    return response.text


## function to retrieve query from the database
def read_sql_query(sql,db):
    conn= sqlite3.connect(db)
    cur= conn.cursor()
    cur.execute(sql)
    rows= cur.fetchall()
    for row in rows:
        print(row)
    return rows


## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL code.
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.

    For example,
    Example 1 - How many entries of records are present?
    The SQL command will be something like this:
    SELECT COUNT(*) FROM STUDENT;

    Also the SQL code should not have ``` in beginning or end
    and should not include the word SQL in the output.

    Example 2 - Tell me all the students studying in DS class?
    The SQL command will be something like this:
    SELECT * FROM STUDENT WHERE CLASS = "DS";  
    """
]


## STREAMLIT App

st.set_page_config(page_title="I can retrieve any SQL Query")
st.header("Gemini App to retrieve SQL data")

question= st.text_input("Enter your question for the SQL database:",key="input")

submit= st.button("Ask the question")

# if submit button is clicked
if submit:
    response=get_gemini_response(question,prompt)
    response= read_sql_query(response,'students.db')
    st.subheader("The Response is:")
    for row in response:
        print(row)
        st.header(row)
    