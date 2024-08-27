from typing import List, Tuple, Optional

"""
    Finds box IDs that differ by exactly one character.

    :param box_ids: List of box IDs.
    :return: Tuple containing the two IDs that differ by exactly one character.
"""
def find_similar_boxes(box_ids: List[str]) -> Tuple:
    num_ids = len(box_ids)
    for i in range(num_ids):
        for j in range(i + 1, num_ids):
            id1 = box_ids[i]
            id2 = box_ids[j]
            if differ_by_one(id1, id2):
                return id1, id2
    return None, None


"""
    Checks if two box IDs differ by exactly one character.

    :param id1: First box ID.
    :param id2: Second box ID.
    :return: True if the IDs differ by exactly one character, False otherwise.
"""
def differ_by_one(id1: str, id2: str) -> bool:
    if len(id1) != len(id2):
        return False

    diff_count = sum(c1 != c2 for c1, c2 in zip(id1, id2))
    return diff_count == 1


"""
    Finds the common letters between two box IDs that differ by exactly one character.

    :param id1: First box ID.
    :param id2: Second box ID.
    :return: String containing the common letters.
"""
def common_letters(id1: str, id2: str) -> str:
    return ''.join(c1 for c1, c2 in zip(id1, id2) if c1 == c2)
