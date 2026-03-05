import zipfile
import os

def extract_logos(zip_path, extract_path):
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # All-logo folder toiri korbe jodi na thake
            if not os.path.exists(extract_path):
                os.makedirs(extract_path)
            
            # Shob file unzip hobe
            zip_ref.extractall(extract_path)
            print(f"Successfully extracted to {extract_path}")
    else:
        print("Zip file khunje paoya jayni!")

if __name__ == "__main__":
    extract_logos('logo.zip', 'All-logo')
