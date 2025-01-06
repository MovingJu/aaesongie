import json

def read_data(file_path):
    """
    Reads JSON data from a given file path.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        dict: Parsed JSON data as a dictionary. Returns an empty dictionary if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {}
    
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return {}