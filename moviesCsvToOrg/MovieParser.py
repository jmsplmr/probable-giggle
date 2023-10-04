from moviesCsvToOrg.Movie import Movie
import warnings


class MovieParser:
    @staticmethod
    def parse_row(row, warn_function=warnings.warn):
        # Ensure the row has at least two elements (title and year)
        if len(row) < 2 or not row[0].strip():
            warn_function(f"Skipping row with invalid title: {row}", UserWarning)
            return None

        title = row[0].strip()
        try:
            year = int(row[1].strip())
        except ValueError:
            warn_function(f"Skipping row with invalid year: {row}", UserWarning)
            return None

        # Parse genres if available
        genres = MovieParser.parse_genres(row[2]) if len(row) > 2 else []

        rating = row[3].strip() if len(row) > 3 else ""
        return Movie(title=title, year=year, genres=genres, rating=rating)

    @staticmethod
    def parse_genres(genres_str):
        return [genre.strip() for genre in genres_str.split(';')]
