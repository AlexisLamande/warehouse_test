from typing import List

"""
    Reads box IDs from a text file.

    :param file_path: Path to the text file.
    :return: List of box IDs.
"""
def read_input_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        box_ids = file.read().splitlines()
    return box_ids
