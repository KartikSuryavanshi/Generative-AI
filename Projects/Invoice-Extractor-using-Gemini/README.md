# Invoice Extractor using Gemini Pro Vision

An intelligent invoice extraction application powered by Google's Gemini Pro Vision model. This tool leverages advanced computer vision and generative AI to automatically extract and process key information from invoice images.

## Overview

This project provides a user-friendly web interface built with Streamlit that allows users to upload invoice images and extract relevant information using Google's state-of-the-art Gemini 1.5 Flash model. The application can identify and extract details such as invoice numbers, dates, amounts, vendor information, and line items with high accuracy.

## Features

- 📸 **Image Upload**: Easy-to-use interface for uploading invoice images
- 🤖 **AI-Powered Extraction**: Leverages Gemini Pro Vision for intelligent data extraction
- ⚡ **Fast Processing**: Uses Gemini 1.5 Flash model for quick responses
- 🔧 **Customizable Prompts**: Flexible prompt system for tailored extraction
- 🎨 **Web Interface**: Clean, intuitive Streamlit-based UI

## Prerequisites

- Python 3.8 or higher
- Google API key with Gemini API access
- pip (Python package manager)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KartikSuryavanshi/Invoice-Extractor-using-Gemini-Pro-Vision.git
cd Invoice-Extractor-using-Gemini-Pro-Vision
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

To get your API key:
1. Visit [Google AI Studio](https://aistudio.google.com)
2. Create a new API key
3. Copy the key and paste it in the `.env` file

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Steps:

1. **Upload an Invoice**: Click the file uploader to select an invoice image (PNG, JPG, etc.)
2. **Enter Prompt**: Provide specific instructions for what you want to extract from the invoice
3. **Get Results**: The AI model will analyze the image and return extracted information

## Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this file)
└── README.md          # Project documentation
```

## Dependencies

- **streamlit**: Web application framework for Python
- **google-genai**: Google's generative AI library
- **python-dotenv**: Environment variable loader
- **Pillow**: Image processing library (included with streamlit)

## How It Works

1. **Image Upload**: Users upload invoice images through the Streamlit interface
2. **Image Processing**: The image is converted to bytes and formatted for the Gemini API
3. **AI Analysis**: The Gemini Pro Vision model analyzes the image based on the provided prompt
4. **Data Extraction**: The model returns extracted information as text
5. **Display Results**: Results are displayed in the web interface

## API Reference

The application uses the following Google Generative AI components:

- **Model**: `models/gemini-flash-latest`
- **Capability**: Multimodal (text + vision)
- **Input**: Text prompt + invoice image
