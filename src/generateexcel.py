from absl import app
from absl import flags
import os
import json
import pandas as pd

FLAGS = flags.FLAGS

# Define flags
flags.DEFINE_string('folder', r'C:\Users\shanelle\anaconda3\envs\codelabs\ComputerGraphics\data', 'Folder containing JSON files')
flags.DEFINE_string('output', 'output', 'Output directory for Excel files')
flags.DEFINE_boolean('verbose', False, 'Enable verbose output')

def load_massive_dataset(dataset_dir):
    dataset = []

    # Iterate through all JSON files in the directory
    for filename in os.listdir(dataset_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(dataset_dir, filename)
            with open(file_path, 'r') as json_file:
                json_data = json.load(json_file)
                dataset.extend(json_data)  # Extend the dataset with data from the current file

    return dataset

def generate_excel_files(dataset, output_dir):
    for language_data in dataset:
        language_id = language_data['id']
        language_utt = language_data['utt']
        language_annot_utt = language_data['annot_utt']

        # Create a DataFrame for the current language
        df = pd.DataFrame({
            'id': language_id,
            'utt': language_utt,
            'annot_utt': language_annot_utt,
        })

        # Save the DataFrame to an Excel file in the specified output directory
        excel_filename = os.path.join(output_dir, f'en-{language_id}.xlsx')
        df.to_excel(excel_filename, index=False, engine='openpyxl')

def main(argv):
    # Parse flags
    FLAGS(argv)

    # Load flags
    folder = FLAGS.folder
    output = FLAGS.output
    verbose = FLAGS.verbose

    # Load the dataset from the specified folder
    massive_dataset = load_massive_dataset(folder)

    # Create the output directory if it doesn't exist
    os.makedirs(output, exist_ok=True)

    # Generate Excel files in the specified output directory
    generate_excel_files(massive_dataset, output)

    if verbose:
        print("Excel files generated successfully.")


if __name__ == '__main__':
    app.run(main)
