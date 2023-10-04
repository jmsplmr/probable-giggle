import os

from moviesCsvToOrg.FileHandler import FileHandler
from moviesCsvToOrg.MovieFormatter import MovieFormatter
from moviesCsvToOrg.MovieParser import MovieParser
from moviesCsvToOrg.MovieSorter import MovieSorter


class MovieConverter:
    def __init__(self, input_file, output_file=None):
        self.input_file = input_file
        self.output_file = output_file

    def convert_csv_to_org(self):
        raw_data = FileHandler.read_csv(self.input_file)
        print(f"{raw_data}")
        movies = [MovieParser.parse_row(row) for row in raw_data if row]

        # Example: Sort movies by year
        movies = MovieSorter.sort_movies(movies, key_func=lambda x: x.year)

        # If output_file is not provided, use a default name
        if self.output_file is None:
            self.output_file = os.path.splitext(self.input_file)[0] + ".org"

        movies_by_genre = self.group_movies_by_genre(movies)
        formatted_data = MovieFormatter.format_movies(movies_by_genre)
        FileHandler.write_to_org(self.output_file, formatted_data)

    @staticmethod
    def group_movies_by_genre(movies):
        movies_by_genre = {}
        for movie in movies:
            for genre in movie.genres:
                if genre not in movies_by_genre:
                    movies_by_genre[genre] = []
                movies_by_genre[genre].append(movie)
        return movies_by_genre
