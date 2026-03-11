import zipfile
import os
import shutil

def unzip_and_organize_bd():
    zip_file = 'logo.zip'
    extract_to = 'temp_extraction_bd'
    final_folder = 'Bangladesh'

    # 1. Check if the zip file exists
    if not os.path.exists(zip_file):
        print(f"Error: {zip_file} not found!")
        return

    # 2. Extract the zip
    print(f"Extracting {zip_file}...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # 3. Create the 'Bangladesh' folder if it doesn't exist
    if not os.path.exists(final_folder):
        os.makedirs(final_folder)

    # 4. Move files from the internal 'Bangladesh' folder to the root folder
    # Screenshot onujayi zip-er bhetore 'Bangladesh' namer folder ache
    source_path = os.path.join(extract_to, 'Bangladesh')
    
    if os.path.exists(source_path):
        for filename in os.listdir(source_path):
            file_path = os.path.join(source_path, filename)
            if os.path.isfile(file_path):
                shutil.move(file_path, os.path.join(final_folder, filename))
        print(f"Successfully moved logos to {final_folder} folder.")
    else:
        print("Error: Could not find 'Bangladesh' folder inside the zip.")

    # 5. Cleanup
    shutil.rmtree(extract_to)
    print("Cleanup complete.")

if __name__ == "__main__":
    unzip_and_organize_bd()
