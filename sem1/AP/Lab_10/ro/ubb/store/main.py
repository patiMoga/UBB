"""

@author: Vlad Paunescu

Aplicație pentru o firmă de închiriere de filme.

Aplicația stochează:

---> filme: <id>,<titlu>,<descriere>,<gen>
---> clienți: <id>, <nume>, <CNP>

Aplicația care permite:

F1: Adaugă lista de filme si lista de clienți
F2: Sterge lista de filme si lista de clienți
F3: Modifică lista de filme si lista de clienți
F4: Căutare film din lista de filme
F5: Căutare clienți din lista de clienti
F6: Închiriere filme
F7: Returnare filme
F8: Raport cu clienții cu filme închiriate ordonat dupa nume
F9: Raport cu clienții cu filme închiriate ordonat dupa numărul de filme închiriate
F10: Raport cu cele mai inchiriate filme.
F11: Raport cu primi 30% dintre clienti cu cele mai multe filme (nume client și numărul de filme închiriate)
F13: Generalised Repository
F12: Load from files
F13: UniTest





I: F1,F2,F3 - finished
II: F4, F5, F6, F7 - finished
III: F9, F8, F10, F11 - finished

"""
from ro.ubb.store.repository.file_repository import FileRepository
from ro.ubb.store.service.client_service import ClientService
from ro.ubb.store.service.movie_service import MovieService
from ro.ubb.store.service.rent_service import RentService
from ro.ubb.store.ui.console import Console

if __name__ == '__main__':
    movie_repository = FileRepository('movie_repository')
    client_repository = FileRepository('client_repository')
    rent_repository = FileRepository('rent_repository')

    movie_service = MovieService(movie_repository)
    client_service = ClientService(client_repository)
    rent_service = RentService(rent_repository, client_repository)

    console = Console(movie_service, client_service, rent_service)
    print("""\n\u001b[36m       Bun venit in aplicatia de administrare a magazinului MovieRent!\u001b[0m""")
    console.run_console()
