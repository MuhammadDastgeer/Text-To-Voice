# Text-To-Voice

This is a Streamlit web application that converts text or uploaded text/PDF/Word files into voice audio using the Groq API.

## Features

- Input text directly or upload a text, PDF, or Word document.
- Extracts text content from uploaded files.
- Converts the text to speech using the PlayAI TTS model.
- Plays the generated voice audio within the app.
- Allows downloading the generated voice audio as a WAV file.

## Requirements

- Python 3.7 or higher
- Streamlit
- Groq Python SDK
- PyPDF2
- python-docx
- python-dotenv

## Setup

1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

- Choose the input type: write text or upload a text/PDF/Word file.
- If uploading a file, supported formats are `.txt`, `.pdf`, and `.docx`.
- Click the "Generate Voice" button to convert the text to speech.
- Listen to the generated audio and download it if desired.

## Notes

- Ensure you have a valid Groq API key.
- The generated audio is saved as `speech.wav` in the project directory.

## License

This project is licensed under the MIT License.
