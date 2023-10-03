import os
import jsonlines

# Define the directory path where your .jsonl files are located
data_folder = 'data'

# List all the files in the directory with a .jsonl extension
jsonl_files = [f for f in os.listdir(data_folder) if f.endswith('.jsonl')]

# Loop through each .jsonl file and process its contents
for jsonl_file in jsonl_files:
    jsonl_file_path = os.path.join(data_folder, jsonl_file)
    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        for item in jsonlines.Reader(file):
            # Process each JSON object in the file
            print(item)
