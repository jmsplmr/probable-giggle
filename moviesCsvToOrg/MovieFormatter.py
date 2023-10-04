class MovieFormatter:
    @staticmethod
    def format_movies(movies):
        content = "* Movies\n"
        for genre, genre_movies in sorted(movies.items()):
            content += f"** {genre}\n"
            for movie in genre_movies:
                rating_info = f" - {movie.rating}" if movie.rating else ""
                content += f"  - [ ] /{movie.title}/ ({movie.year}){rating_info}\n"
        return content
