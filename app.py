import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from PyPDF2 import PdfReader
import docx

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("Please add GROQ_API_KEY in your .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

st.title("🎤 Text, PDF, Word, PPT to Voice Generator")

option = st.radio("Choose Input Type", ["Write Text", "Upload Text/PDF/Word File"])

text_input = ""
if option == "Write Text":
    text_input = st.text_area("Enter text to convert to voice")
elif option == "Upload Text/PDF/Word File":
    uploaded_file = st.file_uploader("Upload a text/pdf/word file", type=["txt", "pdf", "docx"])
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
        if file_type == "txt":
            text_input = uploaded_file.read().decode("utf-8")
        elif file_type == "pdf":
            reader = PdfReader(uploaded_file)
            text_input = ""
            for page in reader.pages:
                text_input += page.extract_text() or ""
        elif file_type == "docx":
            doc = docx.Document(uploaded_file)
            text_input = " ".join([para.text for para in doc.paragraphs])
        else:
            st.error("Unsupported file type")
        st.text_area("Extracted Content", text_input, height=200)

if text_input:
    model = "playai-tts"
    voice = "Fritz-PlayAI"
    response_format = "wav"
    speech_file_path = "speech.wav"

    if st.button("Generate Voice"):
        try:
            response = client.audio.speech.create(
                model=model,
                voice=voice,
                input=text_input,
                response_format=response_format
            )
            response.write_to_file(speech_file_path)
            st.success("Voice generated successfully!")

            audio_file = open(speech_file_path, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            st.download_button(
                label="Download Voice File",
                data=audio_bytes,
                file_name="speech.wav",
                mime="audio/wav"
            )
        except Exception as e:
            st.error(f"Error generating voice: {e}")
