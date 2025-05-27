import json
import os

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"An unexpected error occurred reading {file_path}: {e}")
        return None

def get_editions():
    editions = []
    for dirpath, dirnames, filenames in os.walk("../years/2024-25"):
        for filename in filenames:
            if filename.lower().endswith('.json'):
                full_path = os.path.join(dirpath, filename)
                data = read_json_file(full_path)
                if data is not None:
                    editions.append({"file_path":full_path, "data":data})
    return editions