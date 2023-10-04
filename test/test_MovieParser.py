import unittest
from unittest.mock import patch, Mock
from moviesCsvToOrg.MovieParser import MovieParser, Movie


class TestMovieParser(unittest.TestCase):
    def test_parse_row_valid(self):
        # Test parsing a valid row
        row = ["Movie1", "2000", "Action;Adventure", "PG"]
        parsed_movie = MovieParser.parse_row(row)

        expected_movie = Movie(title="Movie1", year=2000, genres=["Action", "Adventure"], rating="PG")

        self.assertIsNotNone(parsed_movie)
        self.assertEqual(parsed_movie, expected_movie)

    def test_parse_row_invalid_year(self):
        # Test parsing a row with an invalid year
        with patch('warnings.warn') as mock_warn:
            MovieParser.parse_row(["Movie2", "invalid_year", "Comedy", "D"])

            # Check if a UserWarning was issued
            mock_warn.assert_called_once_with("Skipping row with invalid year: ['Movie2', 'invalid_year', 'Comedy', 'D']", UserWarning)

    def test_parse_row_invalid_title(self):
        # Test parsing a row with an invalid title
        with patch('warnings.warn') as mock_warn:
            MovieParser.parse_row(['', '2000', 'Action', 'PG'])

            # Check if a UserWarning was issued
            mock_warn.assert_called_once_with("Skipping row with invalid title: ['', '2000', 'Action', 'PG']", UserWarning)

    def test_parse_row_missing_genres(self):
        # Test parsing a row with missing genres
        with patch('warnings.warn') as mock_warn:
            MovieParser.parse_row(['Movie3', '1995', '', 'PG-13'])

            # Check if a UserWarning was issued
            mock_warn.assert_called_once_with("Skipping row with invalid year: ['Movie3', '1995', '', 'PG-13']", UserWarning)


if __name__ == '__main__':
    unittest.main()
