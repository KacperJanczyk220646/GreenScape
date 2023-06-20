from dashboard import read_file_from_relative_path


def test_read_file_from_path():
    # Test case 1: Existing file
    file_path = 'path/to/existing_file.txt'
    expected_content = "This is the content of the existing file."
    assert dashboard.read_file_from_relative_path(
        file_path) == expected_content, "Test case 1 failed."

    # Test case 2: Non-existing file
    file_path = 'path/to/non_existing_file.txt'
    assert dash(file_path) is None, "Test case 2 failed."

    # Test case 3: Invalid file path
    file_path = 'invalid/path/file.txt'
    assert read_file_from_path(file_path) is None, "Test case 3 failed."

    # Test case 4: Empty file
    file_path = 'path/to/empty_file.txt'
    expected_content = ""
    assert read_file_from_path(
        file_path) == expected_content, "Test case 4 failed."

    # Add more test cases as needed

    print("All test cases passed.")


# Run the unit tests
test_read_file_from_path()
