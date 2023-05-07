import os
import json


def extract_json_data(file_name):
    """
       Load JSON data from a file.

       This function reads the contents of the specified JSON file and returns
       the loaded data as a Python dictionary.

       Args:
           file_name (str): The name of the JSON file (without the file extension).

       Returns:
           dict: The loaded JSON data as a Python dictionary.
       """
    script_dir = f"{os.getcwd()}\\json_data"
    file_path = os.path.join(script_dir, file_name + ".json")

    with open(file_path) as file:
        expected_data = json.load(file)

    return expected_data
