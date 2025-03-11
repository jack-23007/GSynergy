import os
import pandas as pd

# Define input and output directories
input_folder = "/content/drive/MyDrive/swati assignment/unzipped_data"  # Folder with .dlm files
output_folder = "/content/drive/MyDrive/swati assignment/csv_files"  # Folder for CSV output

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Specify the delimiter (modify if needed)
delimiter = "|"  # Change this based on your file structure

# Loop through all .dlm files in the folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".dlm"):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_name = file_name.replace(".dlm", ".csv")
        output_file_path = os.path.join(output_folder, output_file_name)

        # Read the .dlm file
        try:
            df = pd.read_csv(input_file_path, delimiter=delimiter, encoding="utf-8")

            # Save as CSV
            df.to_csv(output_file_path, index=False, encoding="utf-8")
            print(f"Converted: {file_name} -> {output_file_name}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("All .dlm files have been converted to CSV.")
