from ro.Patricia.Problema3.repository.repository import  Repository
from ro.Patricia.Problema3.service.service import MovieService
from ro.Patricia.Problema3.service.service import ClientService
from ro.Patricia.Problema3.service.service import RentService
from ro.Patricia.Problema3.test.testAll import testAll
from ro.Patricia.Problema3.ui.console import Console

if __name__ == '__main__':
    testAll()
    movieRepository=Repository('movie_save_file')
    clientRepository = Repository('client_save_file')
    rentMovieRepository=Repository('rent_save_file')
    movieService=MovieService(movieRepository)
    clientService=ClientService(clientRepository)
    rentMovieService=RentService(rentMovieRepository,clientRepository)
    console= Console(clientService, movieService, rentMovieService)
    console.menu()