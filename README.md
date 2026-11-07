
# AI Document Assistant

A Python web application that uses a local AI model to analyze architecture project documents.

## Features
- Upload TXT documents
- Generate AI-powered document summaries
- Ask questions about uploaded documents
- Extract project details such as budgets and deadlines
- Run AI locally without paid API access

## Technologies
- Python
- Streamlit
- Ollama
- Llama 3.2 (1B)

## How to Run

1. Install Python and Ollama.
2. Download the AI model:

   ollama pull llama3.2:1b

3. Install Python dependencies:

   python -m pip install -r requirements.txt

4. Start the application:

   python -m streamlit run app.py

5. Open the local URL shown in the terminal.

## Project Purpose

This independent portfolio project demonstrates
AI integration, document processing, web application
development, and practical automation for architecture teams.

## Limitations

- Supports TXT files only.
- Requires Ollama running locally.
- AI responses should be checked against source documents.
