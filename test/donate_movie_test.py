import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Movie(object):
    imdb_id: str


@dataclass
class Library(object):
    movies: List[Movie]

    def find_movie(self, imdb_id):
        return next(filter(lambda movie: movie.imdb_id == imdb_id, self.movies))


class MyTestCase(unittest.TestCase):
    def test_finds_movie_by_id(self):
        imdb_id = "tt1234"
        movie = Movie(imdb_id)
        library = Library([movie])
        self.assertEqual(imdb_id, library.find_movie(imdb_id).imdb_id)

    def test_adds_movie_to_library(self):
        pass


if __name__ == '__main__':
    unittest.main()
