import zipfile
import os

def extract_logos(zip_path, extract_path):
    if os.path.exists(zip_path):
        # All-logo folder fresh bhabe toiri korbe
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
            
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f"Done! Logos are now in {extract_path}")
    else:
        print("logo.zip not found!")

if __name__ == "__main__":
    extract_logos('logo.zip', 'All-logo')
