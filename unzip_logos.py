import zipfile
import os
import shutil

def extract_logos(zip_path, extract_path):
    if not os.path.exists(zip_path):
        print("logo.zip not found!")
        return

    temp_folder = "temp_extract"
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
    os.makedirs(temp_folder)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)

    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)
    os.makedirs(extract_path)

    # Shudhu .png ebong .md file gulo ke nibe
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            # Eikhane extension check kora hochhe
            if file.lower().endswith(('.png', '.md')):
                shutil.move(os.path.join(root, file), os.path.join(extract_path, file))

    shutil.rmtree(temp_folder)
    print(f"Success! Logos and MD files are now in {extract_path}")

if __name__ == "__main__":
    extract_logos('logo.zip', 'India')
