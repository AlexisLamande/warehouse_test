from collections import Counter
from typing import List

"""
    Calculates the checksum based on the list of box IDs.

    :param box_ids: List of box IDs.
    :return: Calculated checksum.
"""
def calculate_checksum(box_ids: List[str]) -> int:
    two_count = 0
    three_count = 0

    for box_id in box_ids:
        letter_count = Counter(box_id)
        has_two = 2 in letter_count.values()
        has_three = 3 in letter_count.values()

        if has_two:
            two_count += 1
        if has_three:
            three_count += 1

    return two_count * three_count
