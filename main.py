from src.checksum import calculate_checksum, read_input_file
from src.checksum.box_comparator import find_similar_boxes, common_letters

def main():
    # Read the IDs from the "input.txt" file
    box_ids = read_input_file('resources/input.txt')

    # Calculate the checksum
    checksum = calculate_checksum(box_ids)
    print(f"\nThe calculated checksum is: {checksum}\n")

    # Find the boxes that differ by exactly one character
    id1, id2 = find_similar_boxes(box_ids)
    if id1 and id2:
        print(f"The two box IDs that differ by exactly one character are: {id1} and {id2}\n")
        # Find and display the common letters between these two IDs
        common = common_letters(id1, id2)
        print(f"The common letters between these two IDs are: {common}\n")
    else:
        print("No pair of box IDs differs by exactly one character.\n")

if __name__ == "__main__":
    main()
