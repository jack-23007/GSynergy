import os
import pandas as pd

# Define the folder containing CSV files
csv_folder = "/content/drive/MyDrive/swati assignment/csv_files"

# List all CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith(".csv")]

# Read and display each CSV file
for file_name in csv_files:
    file_path = os.path.join(csv_folder, file_name)

    # Read the CSV file
    df = pd.read_csv(file_path, encoding="utf-8")

    # Display file name and content
    print(f"\n{'='*40}\nFile: {file_name}\n{'='*40}")
    display(df) 
