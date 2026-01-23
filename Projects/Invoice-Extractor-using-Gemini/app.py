## Invoice Extractor

from dotenv import load_dotenv
import os

load_dotenv() ## Load environment variables from .env file

import streamlit as st
from PIL import Image
import io
from google import genai
from google.genai.types import Part

## configure the API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro vision model and get response

def get_gemini_response(input_text, image, prompt):
    ## Use gemini 1.5 flash model (supports vision)
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=[
            {
                "role": "user",
                "parts": [
                    Part.from_text(text=input_text),
                    image[0],
                    Part.from_text(text=prompt),
                ],
            }
        ],
    )
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            Part.from_bytes(data=bytes_data, mime_type=uploaded_file.type)
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

## initializing the streamlit app

st.set_page_config(page_title="Invoice Extractor", page_icon=":robot_face:")

st.header("Invoice Extractor using Gemini Pro Vision")
input=st.text_input("Input prompt: ",key="input")
uploaded_file = st.file_uploader("Upload an invoice image", type=["png", "jpg", "jpeg"])
image=""
if uploaded_file is not None:
    # Ensure robust image decoding from uploaded bytes
    image = Image.open(io.BytesIO(uploaded_file.getvalue()))
    st.image(image, caption='Uploaded Invoice Image.')

submit_button=st.button(label="Tell me the details from the invoice")

input_prompts="""
You are an expert in understanding invoices. You will recieve input images as invoices and you will have to answer questions based on the input image.
"""

## if submit button is pressed
if submit_button:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompts,image_data,input)
    st.subheader("Response from Gemini Pro Vision:")
    st.write(response)

 
        