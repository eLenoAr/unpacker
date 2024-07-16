import os
import sys
import subprocess
import glob

def find_r01_files(directory):
    r01_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".r01"):
                r01_files.append(os.path.join(root, file))
    return r01_files

def replace_extension_with_rar(file_path):
    base = os.path.splitext(file_path)[0]
    return base + ".rar"

def extract_files(rar_file_path):
    try:
        rar_file_dir = os.path.dirname(rar_file_path)
        unrar_command = ["rar", "x", "-o-", rar_file_path, rar_file_dir]
        result = subprocess.run(unrar_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"Extracted: {rar_file_path}")
            return True
        elif result.returncode == 1:
            print(f"Error: Generic error occurred while extracting {rar_file_path}")
            return False
        else:
            print(f"Error: Extraction failed with exit code {result.returncode} for {rar_file_path}")
            return False
        
        
    except subprocess.CalledProcessError as e:
        if e.returncode == 10:
            print(f"Skipped extracting {rar_file_path}: Files already exist.")
            return True
        else:
            print(f"Error extracting {rar_file_path}: {e}")
            return False

def delete_files(files_to_delete):
    for file_path in files_to_delete:
        # print(f"Deleting: {file_path}")
        os.remove(file_path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python unpack.py <search_directory>")
        return
    
    search_directory = sys.argv[1]
    
    if not os.path.isdir(search_directory):
        print(f"Error: {search_directory} is not a valid directory.")
        return

    r01_files = find_r01_files(search_directory)

    
    
    failed_extractions = []

    if not r01_files:
        print("No .r01 files found.")
    else:
        amount_of_r01_files = len(r01_files)
        current_count = 1
        print(f"Found {amount_of_r01_files} releases.")
        
        for r01_file in r01_files:
            print(f"Found: {os.path.dirname(r01_file)} -- {current_count} of {amount_of_r01_files}")

            all_extracted_successfully = True
            files_to_delete = []
            
            rar_file = replace_extension_with_rar(r01_file)
            files_to_delete.extend(glob.glob(rar_file.replace(".rar", ".r*")))
            files_to_delete.append(rar_file.replace(".rar", ".sfv"))

            if not extract_files(rar_file):
                all_extracted_successfully = False
                continue

            if all_extracted_successfully:
                print(f"Deleted {len(files_to_delete)} files in {os.path.dirname(rar_file)}")
                delete_files(files_to_delete)
            else:
                failed_extractions.append(rar_file)
                print("Extraction failed, no files were deleted.")
            
            current_count += 1
    
    if failed_extractions:
        print(f"Failed to extract {len(failed_extractions)} files:")
        for failed_extraction in failed_extractions:
            print(failed_extraction)

if __name__ == "__main__":
    main()
