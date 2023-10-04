class MovieSorter:
    @staticmethod
    def sort_movies(movies, key_func):
        return sorted(movies, key=key_func)
