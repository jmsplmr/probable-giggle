from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    year: int
    genres: list
    rating: str
