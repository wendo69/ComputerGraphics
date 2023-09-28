"""
This is the main file for the project.
"""
import pandas as pd
from generateexcel import main  # Import the main function from generateexcel.py
from loaddataset import load_massive_dataset

if __name__ == "__main__":
    massive_dataset = load_massive_dataset()
    # Perform operations on the combined dataset as needed

    # Call the Excel file generation process from generateexcel.py
    main(["generateexcel.py"])  # Pass the program name as the first element of argv
