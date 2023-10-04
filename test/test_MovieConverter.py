import difflib
import unittest
import tempfile
import os
from moviesCsvToOrg.MovieConverter import MovieConverter


class TestMovieConverter(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.csv_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".csv").name
        with open(self.csv_file_path, 'w') as csvfile:
            csvfile.write("Movie1,2000,Action;Adventure,PG\n")
            csvfile.write("Movie2,1995,Action,PG-13\n")
            csvfile.write("Movie3,1990,Comedy,R\n")

    def tearDown(self):
        # Remove the temporary CSV file after testing
        os.remove(self.csv_file_path)

    def test_convert_csv_to_org(self):
        # Test converting CSV to Org format
        output_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".org").name

        converter = MovieConverter(input_file=self.csv_file_path, output_file=output_file_path)
        converter.convert_csv_to_org()

        # Read the content of the generated Org file
        with open(output_file_path, 'r') as orgfile:
            org_content = orgfile.read()

        expected_content = """* Movies
** Action
 - [ ] /Movie2/ (1995) - PG-13
 - [ ] /Movie1/ (2000) - PG
** Adventure
 - [ ] /Movie1/ (2000) - PG
** Comedy
 - [ ] /Movie3/ (1990) - R
"""

        # Use difflib to visualize the differences
        diff = difflib.unified_diff(expected_content.splitlines(), org_content.splitlines(), lineterm='')
        diff_str = '\n'.join(diff)

        # Modify the assertion
        self.assertTrue(''.join(org_content.split()) == ''.join(expected_content.split()), f"Differences:\n{diff_str}")


if __name__ == '__main__':
    unittest.main()
