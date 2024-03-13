from masina import Masina
from functii import *
if __name__ == "__main__":
    a = []
    f = open("date.txt", "r")
    for x in f:
        date = x.split()
        marca = date[0]
        model = date[1]
        tokenMasina = date[2]
        pretVanzare = date[3]
        pretAchizitie = date[4]
        masina = Masina(marca, model, tokenMasina, pretVanzare,pretAchizitie)
        a.append(masina)
    optiune = input("optiune: ")
    lista = optiune.split()
    if len(lista) == 2:
        lista.append('0')
        lista.append('0')
    elif len(lista) == 3:
        lista.append('0')
    if(lista[0] == 'SORT'):
        lista.pop(0)
        sort_alg(a, lista)
    if(lista[0] == 'SEARCH'):
        masina = search(a, lista[1])
        print(masina.model + " " + masina.marca + " " + masina.tokenMasina + " " + " " + masina.pretVanzare + " " + masina.pretAchizitie)

    for list in a:
        print(list.model + " " + list.marca + " " + list.tokenMasina + " " + list.pretAchizitie)