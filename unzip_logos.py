import zipfile
import os
import shutil

def extract_logos(zip_path, extract_path):
    if not os.path.exists(zip_path):
        print("logo.zip not found!")
        return

    # Temporary folder create kora
    temp_folder = "temp_extract"
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
    os.makedirs(temp_folder)

    # Extract kora
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)

    # Main "All-logo" folder create kora
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)
    os.makedirs(extract_path)

    # Shudhu .png file gulo ke All-logo folder-e move kora
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.lower().endswith('.png'):
                shutil.move(os.path.join(root, file), os.path.join(extract_path, file))

    # Temporary folder delete kora
    shutil.rmtree(temp_folder)
    print(f"Success! All logos are now in {extract_path}")

if __name__ == "__main__":
    extract_logos('logo.zip', 'All-logo')
