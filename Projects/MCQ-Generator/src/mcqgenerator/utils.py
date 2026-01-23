import os
import io
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            # Ensure we have a fresh stream at position 0
            if hasattr(file, "seek"):
                file.seek(0)

            # Streamlit UploadedFile may need wrapping in BytesIO
            reader_input = file
            if isinstance(getattr(file, "read", None), object):
                raw = file.read()
                # Reset position for any further reads
                if hasattr(file, "seek"):
                    file.seek(0)
                reader_input = io.BytesIO(raw)

            pdf_reader = PyPDF2.PdfReader(reader_input)
            text = ""
            for page in pdf_reader.pages:
                content = page.extract_text() or ""
                text += content
            return text

        except Exception as e:
            raise Exception("error reading the PDF file")

    elif file.name.endswith(".txt"):
        if hasattr(file, "seek"):
            file.seek(0)
        return file.read().decode("utf-8")

    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
        )

def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]
        
        # iterate over the quiz dictionary and extract the required information
        for key,value in quiz_dict.items():
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                 
                 ]
            )
            
            correct=value["correct"]
            quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})
        
        return quiz_table_data
        
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False

