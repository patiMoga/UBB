from ro.Patricia.Problema3.repository.repository import Repository
from ro.Patricia.Problema3.service.service import MovieService


def testAddMovie():
    testMovieRepository=Repository('test_save_file')
    testMovieService = MovieService(testMovieRepository)
    testMovieService.add_entity(testMovieService.create_movie(0, 'Hello', 'World', '!'))
    assert len(testMovieService.get_all_entities()) == 1
    #testMovieService.create_movie(0, 'Hello', 'World', '!')

def testDeleteMovie():
    testMovieRepository = Repository('test_save_file')
    testMovieService = MovieService(testMovieRepository)
    testMovieService.add_entity(testMovieService.create_movie(0, 'Hello', 'World', '!'))
    testMovieService.delete_entity(0)
    assert len(testMovieService.get_all_entities()) == 0

def testGetMovieById():
    testMovieRepository = Repository('test_save_file')
    testMovieService = MovieService(testMovieRepository)
    testMovieService.add_entity(testMovieService.create_movie(0, 'Hello', 'World', '!'))
    assert testMovieService.get_entity_by_id(1) is None

def testUpdateMovie():
    testMovieRepository = Repository('test_save_file')
    testMovieService = MovieService(testMovieRepository)
    testMovieService.add_entity(testMovieService.create_movie(0, 'Hello', 'World', '!'))
    testMovieService.update_entity(testMovieService.create_movie(0, 'Hello', 'World', '!'))