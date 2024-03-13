from repository.cafea_repository import Repository
from service.cafea_service import CafeaService
from teste.test_all import test_all
from ui.console import CafeaConsole

if __name__ == '__main__':
    test_all()
    cafea_repository = Repository()
    cafea_service = CafeaService(cafea_repository)
    cafea_console = CafeaConsole(cafea_service)

    cafea_console.run_console()