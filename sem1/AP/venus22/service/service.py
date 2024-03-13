class Service:
    def __init__(self,repo):
        self.repo=repo
    def add_avi(self,avion):
        self.repo.add_avi(avion)
    def delete(self,id):
        self.repo.delete_avi(id)
    def save(self):
        self.repo.save()
    def load(self):
        self.repo.load()

    def ord(self):
        lista=self.repo.avioane
        lista=sorted(lista,key=lambda avion: avion.maxpas, reverse=True)
        l=""
        for a in lista:
            l=l+str(a)+"\n"
        return l
    def print(self):
        return str(self.repo)