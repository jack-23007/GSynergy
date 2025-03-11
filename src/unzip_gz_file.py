import gzip
import shutil
import os

# List of gzip files
gz_files = [
    "/content/drive/MyDrive/swati assignment/data/hier.clnd.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.invloc.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.hldy.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.possite.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.pricestate.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.invstatus.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/fact.averagecosts.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.rtlloc.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/hier.prod.dlm.gz",
    "/content/drive/MyDrive/swati assignment/data/fact.transactions.dlm.gz"
]

# Destination folder
output_folder = "/content/drive/MyDrive/swati assignment/unzipped_data"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each .gz file and extract
for gz_file in gz_files:
    # Extract the filename without .gz extension
    file_name = os.path.basename(gz_file).replace('.gz', '')
    output_file_path = os.path.join(output_folder, file_name)

    # Unzip the file
    with gzip.open(gz_file, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    print(f"Extracted: {file_name} -> {output_file_path}")

print("All files have been extracted successfully.")