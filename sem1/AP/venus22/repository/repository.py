from domain.avion import Avion

class RepoAvioane:
    def __init__(self):
        self.avioane=[]
    def add_avi(self,avion):
        for a in self.avioane:
            if a.id==avion.id:
                raise ValueError("Id existent")
        self.avioane.append(avion)

    def delete_avi(self,id):
        lista=[]
        for a in self.avioane:
            if a.id!=id:
                lista.append(a)
        self.avioane=lista

    def save(self):
        fisier=open("avioane.txt","w")
        lista=[]
        for a in self.avioane:
            lista.append(a.__dict__)
        fisier.write(str(lista))

    def load(self):
        fisier=open("avioane.txt","r")
        l=eval(fisier.read())
        self.avioane=[]

        for d in l:
            avion=Avion(d["id"],d["model"],d["maxpas"])
            self.avioane.append(avion)

    def __str__(self):
        l=""
        for a in self.avioane:
            l=l+str(a)+"\n"
        return l
