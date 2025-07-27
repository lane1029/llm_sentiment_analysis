# Sentiment Analysis with Ollama LLM
This Python script performs sentiment analysis on qualitative interview data using a local large language model (LLM) served via Ollama. It reads question-answer pairs from a CSV file, invokes a specified LLM model, and extracts structured sentiment data with associated confidence scores and evidence. Results are stored in a CSV for further analysis.

## Project Structure
`.
├── sentiment_analysis_ollama.py     # Main script
├── excerpts_folder/                 # Folder with input CSV files
│   └── your_file.csv                # CSV with question, answer, and id columns
├── sentiments/                      # Output folder for annotated CSV files
├── ollama.log                       # Log file for Ollama server output
`

## Requirements
- Python 3.8+
- Ollama installed and available on your system path
- Python dependencies:
`pip install langchain-ollama pandas psutil`
