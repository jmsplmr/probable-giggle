import unittest
from moviesCsvToOrg.MovieConverter import MovieFormatter
from moviesCsvToOrg.Movie import Movie


class TestMovieFormatter(unittest.TestCase):
    def test_format_movies(self):
        # Test formatting movies by genre
        movies = {
            "Action": [
                Movie(title="Movie1", year=2000, genres=["Action"], rating="PG-13"),
                Movie(title="Movie2", year=1995, genres=["Action"], rating="R")
            ],
            "Comedy": [
                Movie(title="Movie3", year=1990, genres=["Comedy"], rating="PG"),
                Movie(title="Movie4", year=1998, genres=["Comedy"], rating="")
            ]
        }

        formatted_content = MovieFormatter.format_movies(movies)

        expected_content = """* Movies
** Action
  - [ ] /Movie1/ (2000) - PG-13
  - [ ] /Movie2/ (1995) - R
** Comedy
  - [ ] /Movie3/ (1990) - PG
  - [ ] /Movie4/ (1998)
"""

        self.assertEqual(formatted_content, expected_content)


if __name__ == '__main__':
    unittest.main()
