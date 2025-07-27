import os
import csv
import json
# dependency: pip install langchain-ollama
from langchain_ollama import OllamaLLM
import pandas as pd
import re
import subprocess
import time
import psutil  # pip install psutil

# Build the prompt for the LLM (template function)
def build_prompt(question, answer):
    #UPDATE: Add your prompt template here. See build_prompt_fns/knowledge_atrophy.py for an example.
    return prompt

# Kill any running Ollama processes
def kill_ollama():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        name = proc.info.get('name') or ""
        cmdline = proc.info.get('cmdline') or []
        if "ollama" in name or any("ollama" in c for c in cmdline):
            print(f"🔪 Killing Ollama pid=`{proc.info['pid']}")
            proc.kill()
            proc.wait()

# Start Ollama server and log output
def start_ollama():
    print("🚀 Starting Ollama")
    with open('ollama.log', 'a') as log:
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=log,
            stderr=log
        )
    time.sleep(30)  # wait for it to start

# Restart Ollama server (kill and start)
def restart_ollama():
    kill_ollama()
    start_ollama()

# Clean up and fix malformed JSON strings from LLM output
def clean_json_string(json_str):
    """
    Bulletproof cleaner:
    - Preserves valid `""`
    - Fixes truly missing values
    - Escapes unescaped quotes
    - Fixes trailing `""`
    - Removes incorrect leading `\`
    """

    # 🔷 Remove invalid escape of single quotes
    json_str = json_str.replace(r"\'", "'")

    # Remove incorrect leading slash
    json_str = re.sub(
        r'(".*?")\s*:\s*\\+"',
        r'\1: "',
        json_str
    )

    # Escape unescaped inner quotes (but preserve empty strings)
    def escape_inner_quotes(match):
        key, value = match.group(1), match.group(2)
        if value == "":
            return f'"{key}": ""'
        fixed_value = re.sub(r'(?<!\\)"', r'\\"', value)
        return f'"{key}": "{fixed_value}"'

    json_str = re.sub(
        r'"([^"]+)"\s*:\s*"([^"]*)"',
        escape_inner_quotes,
        json_str
    )

    # Fix trailing double quotes
    json_str = re.sub(
        r'(":.*?[^\\])("")(\s*[},])',
        r'\1\3',
        json_str,
        flags=re.DOTALL
    )

    # Fix only truly missing values: key followed by colon & *nothing* (not even `""`)
    json_str = re.sub(
        r'(".*?")\s*:\s*(?=[},])',
        lambda m: f'{m.group(1)}: ""',
        json_str
    )

    return json_str

# Normalize JSON keys and fill in missing expected keys
def normalize_json_keys(parsed_json, expected_keys):
    """
    Ensures all expected keys are present and maps obvious miskeys.
    """
    normalized = {}

    # map common wrong key names to correct keys
    # UPDATE: this is now empty, but you can add mappings if needed
    # e.g. "sentiment" → "knowledge_atrophy_sentiment"
    key_aliases = {
    }

    # handle known alias/mistakes
    for wrong_key, correct_key in key_aliases.items():
        if wrong_key in parsed_json:
            value = parsed_json.pop(wrong_key)
            # convert boolean True → string "not_mentioned"
            if isinstance(value, bool) and value:
                value = "not_mentioned"
            normalized[correct_key] = value

    # fill in all expected keys
    for k in expected_keys:
        if k in parsed_json:
            normalized[k] = parsed_json[k]
        elif k not in normalized:
            normalized[k] = expected_keys[k]  # default None

    # include any other keys that are unexpected
    for k, v in parsed_json.items():
        if k not in normalized:
            normalized[k] = v

    return normalized

# This script processes files in the specified folder structure, extracting sentiment analysis from LLM responses.
# Input files paths
base_file_path = os.getcwd()
# UPDATE: Change this to your actual path to the excerpts folder
excerpts_file_path = os.path.join(base_file_path, "excerpts_folder")

# Create 'sentiments' folder if it doesn't exist
# UPDATE: Change this to your actual path to the sentiments folder
sentiments_folder_path = os.path.join(base_file_path, "sentiments")
os.makedirs(sentiments_folder_path, exist_ok=True)

# Specify the model to use
restart_ollama()
model = OllamaLLM(model="deepseek-r1:latest")
counter = 0

# Process a single file containing question-answer pairs
# UPDATE: Set the path to your single file here
single_file_path = os.path.join(excerpts_file_path, "your_file.csv") 

if not os.path.isfile(single_file_path):
    raise FileNotFoundError(f"File not found: {single_file_path}")

print(f"Processing file: {single_file_path}")

# Output folder for single file (optional: use a fixed name or derive from file)
output_folder_path = sentiments_folder_path
os.makedirs(output_folder_path, exist_ok=True)

file_name = os.path.basename(single_file_path)
df = pd.read_csv(single_file_path)

for index, row in df.iterrows():
    # Extract question, answer, and id from the current row
    question = row['question']
    answer = row['text']
    id = row['id']
    print(f"Processing row {index+1}/{len(df)}")

    # Build the prompt for the LLM using the question and answer
    prompt = build_prompt(question, answer)

    # Invoke the LLM model with the prompt
    result = model.invoke(input=prompt)
    print(result)

    # Extract any <think>...</think> blocks from the result for thought process
    think_matches = re.findall(r"<think>(.*?)</think>", result, re.DOTALL | re.IGNORECASE)
    combined_thoughts = "\n\n---\n\n".join([t.strip() for t in think_matches if t.strip()])

    # Extract JSON objects from the result
    json_matches = re.findall(r"\{[\s\S]*?\}", result)
    if not json_matches:
        raise ValueError("No JSON found in response.")

    # Use the last JSON object found
    last_json_text = json_matches[-1].strip()
    last_json_text = clean_json_string(last_json_text)

    # Parse the cleaned JSON string
    try:
        parsed_result = json.loads(last_json_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON: {e}\nJSON text:\n{last_json_text}")

    # Define expected keys for the output
    # UPDATE as needed for your prompt
    expected_keys = {
        "knowledge_atrophy_sentiment": None,
        "knowledge_atrophy_sentiment_confidence_score": None,
        "knowledge_atrophy_sentiment_evidence": None
    }

    # Normalize the parsed JSON to ensure all expected keys are present
    parsed_result = normalize_json_keys(parsed_result, expected_keys)
    parsed_result["thought_process"] = combined_thoughts

    # Write results back to the DataFrame
    # UPDATE: column names as needed
    df.at[index, 'knowledge_atrophy_sentiment'] = parsed_result['knowledge_atrophy_sentiment']
    df.at[index, 'knowledge_atrophy_sentiment_confidence_score'] = parsed_result['knowledge_atrophy_sentiment_confidence_score']
    df.at[index, 'knowledge_atrophy_sentiment_evidence'] = parsed_result['knowledge_atrophy_sentiment_evidence']
    df.at[index, 'knowledge_atrophy_sentiment_thought_process'] = parsed_result['thought_process']

    # Restart Ollama server every 10 rows to avoid issues (ie. memory leaks, timeouts, etc.)
    counter += 1
    if counter > 10:
        restart_ollama()
        model = OllamaLLM(model="deepseek-r1:latest")
        counter = 0

# Save the updated DataFrame to output folder
output_file_path = os.path.join(output_folder_path, file_name)
df.to_csv(output_file_path, index=False)
print(f"Saved results to {output_file_path}")
