import unittest
from moviesCsvToOrg.MovieConverter import MovieSorter


class TestMovieSorter(unittest.TestCase):
    def test_sort_movies_by_year(self):
        # Test sorting movies by year
        movies = [
            {"title": "Movie2", "year": 1995},
            {"title": "Movie1", "year": 2000},
            {"title": "Movie3", "year": 1990}
        ]

        sorted_movies = MovieSorter.sort_movies(movies, key_func=lambda x: x["year"])

        expected_order = [
            {"title": "Movie3", "year": 1990},
            {"title": "Movie2", "year": 1995},
            {"title": "Movie1", "year": 2000}
        ]

        self.assertEqual(sorted_movies, expected_order)


if __name__ == '__main__':
    unittest.main()
