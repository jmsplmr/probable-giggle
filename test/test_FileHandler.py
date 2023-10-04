import os
import unittest
from tempfile import NamedTemporaryFile

from moviesCsvToOrg.MovieConverter import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.csv_file = NamedTemporaryFile(mode='w+', delete=False, suffix='.csv')
        self.csv_file_name = self.csv_file.name

        # Write some data to the CSV file
        self.csv_file.write("Title,Year,Genres,Rating\n")
        self.csv_file.write("Movie1,2000,Action;Adventure,PG\n")
        self.csv_file.write("Movie2,1995,Comedy,D\n")
        self.csv_file.flush()

    def tearDown(self):
        # Remove the temporary CSV file after testing
        os.remove(self.csv_file_name)

    def test_read_csv(self):
        # Test reading from the CSV file
        file_data = FileHandler.read_csv(self.csv_file_name)
        expected_data = [
            ['Title', 'Year', 'Genres', 'Rating'],
            ['Movie1', '2000', 'Action;Adventure', 'PG'],
            ['Movie2', '1995', 'Comedy', 'D']
        ]
        self.assertEqual(file_data, expected_data)

    def test_write_to_org(self):
        # Test writing to an Org file
        org_file = NamedTemporaryFile(mode='w+', delete=False, suffix='.org')
        org_file_name = org_file.name
        content = "Sample Org Content"

        FileHandler.write_to_org(org_file_name, content)

        # Verify that the Org file contains the expected content
        with open(org_file_name, 'r', encoding='utf-8') as orgfile:
            written_content = orgfile.read()
            self.assertEqual(written_content, content)

        # Clean up the temporary Org file
        os.remove(org_file_name)


if __name__ == '__main__':
    unittest.main()
