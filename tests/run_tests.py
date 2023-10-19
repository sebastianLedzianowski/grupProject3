import pytest

if __name__ == "__main__":
    # List of test files to run
    test_files = ["test_contact_book.py", "test_note_book.py"]

    # Run pytest and pass the list of test files
    pytest.main(test_files)