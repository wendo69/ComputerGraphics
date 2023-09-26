import os
import json

def load_massive_dataset():
    dataset_dir = 'data'  # Replace with the directory containing your JSON files
    dataset = []

    # Iterate through all JSON files in the directory
    for filename in os.listdir(dataset_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(dataset_dir, filename)
            with open(file_path, 'r') as json_file:
                json_data = json.load(json_file)
                dataset.extend(json_data)  # Extend the dataset with data from the current file

    return dataset

if __name__ == "__main__":
    massive_dataset = load_massive_dataset()
    # Perform operations on the combined dataset as needed
