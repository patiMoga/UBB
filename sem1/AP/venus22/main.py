from repository.repository import RepoAvioane
from service.service import Service
from ui import console

if __name__=="__main__":
    repo=RepoAvioane()
    serv=Service(repo)
    console.consola(serv)



