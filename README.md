# Sentiment Analysis with Ollama LLM
This Python script performs sentiment analysis on qualitative interview data using a local large language model (LLM) served via Ollama. It reads question-answer pairs from a CSV file, invokes a specified LLM model, and extracts structured sentiment data with associated confidence scores and evidence. Results are stored in a CSV for further analysis.

## Project Structure
<pre>
.
├── sentiment_analysis_ollama.py     # Main script
├── excerpts_folder/                 # Folder with input CSV files
│   └── your_file.csv                # CSV with question, answer, and id columns
├── sentiments/                      # Output folder for annotated CSV files
├── ollama.log                       # Log file for Ollama server output

</pre>
## Requirements
- Python 3.8+
- Ollama installed and available on your system path
- Python dependencies:
`pip install langchain-ollama pandas psutil`

## Input Format
Each input file should be a CSV (.csv) with the following columns:
- id: A unique identifier for each interview pair
- question: The interview question
- text: The corresponding answer or response

## Running the Script
1. Place your input file in the excerpts_folder/ directory.
2. Update the following paths in the script:
<pre>
excerpts_file_path = os.path.join(base_file_path, "excerpts_folder")
single_file_path = os.path.join(excerpts_file_path, "your_file.csv")
</pre>
3. Customize your prompt by editing the build_prompt(question, answer) function.
4. Run the script:
<pre> python sentiment_analysis_ollama.py </pre>
