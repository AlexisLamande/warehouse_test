# The Warehouse

This project solves a checksum problem involving box IDs. It includes functionality to calculate a checksum based on the box IDs and to find pairs of box IDs that differ by exactly one character.

## Project Structure

The project is organized as follows:

- **`src/`**: Contains the main source code.
    - **`checksum/`**:
        - **`checksum_calculator.py`**: Contains the function to calculate the checksum.
        - **`file_reader.py`**: Contains the function to read box IDs from a file.
        - **`box_comparator.py`**: Contains functions to find similar boxes and common letters.
- **`tests/`**: Contains unit tests for the functions in `src/`.
    - **`test_checksum_calculator.py`**: Tests for the checksum calculation.
    - **`test_file_reader.py`**: Tests for file reading functionality.
    - **`test_box_comparator.py`**: Tests for box comparison and common letters functions.
- **`main.py`**: The entry point for the program that executes the main functionality.
- **`requirements.txt`**: Lists the Python dependencies for the project.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/AlexisLamande/warehouse_test.git
    cd warehouse_test
    ```

2. **Install Dependencies**

   Ensure you have Python installed. Then, install the required Python packages. In our case, no package is required :

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Main Program**

   To execute the main program, use the following command:

    ```bash
    python main.py
    ```

   This will read the box IDs from `resources/input.txt`, calculate the checksum, and find box IDs that differ by exactly one character.

## Running Tests

To ensure that all functions work correctly, you can run the unit tests:

- **Using `unittest`**:

    ```bash
    python -m unittest discover -s tests
    ```

## Improvements

If the application is to be expanded or enhanced, here are some potential improvements:

- **Performance Optimization**:
    - For very large datasets, consider optimizing the `find_similar_boxes` function to improve performance and reduce memory usage.

- **Error Handling**:
    - Add more robust error handling for file operations and input validation to handle edge cases and potential issues gracefully.

- **Configuration Management**:
    - Implement a configuration file or command-line arguments to allow dynamic input file paths and other parameters.

- **Logging**:
    - Introduce logging to track the application's execution and facilitate debugging and monitoring.

- **Documentation**:
    - It might also be helpful to generate project documentation using an appropriate tool.
