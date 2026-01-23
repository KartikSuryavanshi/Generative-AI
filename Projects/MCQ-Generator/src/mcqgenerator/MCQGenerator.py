import os
from dotenv import load_dotenv
from operator import itemgetter

# importing necessary packages from langchain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


# Load environment variables from .env file
load_dotenv()

# Access the environment variables just like you do with os.environ
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OPENAI_API_KEY is not set. Please add it to your environment or .env file.")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=key)

template="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template)


quiz_chain = quiz_generation_prompt | llm | StrOutputParser()

template2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""


quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=template2,
)

review_chain = (
    {"subject": itemgetter("subject"), "quiz": quiz_chain}
    | quiz_evaluation_prompt
    | llm
    | StrOutputParser()
)

# Overall pipeline that returns both the quiz and the review
generate_evaluate_chain = RunnableParallel(quiz=quiz_chain, review=review_chain)