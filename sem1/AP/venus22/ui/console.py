from domain.avion import Avion


def consola(serv):
    while True:
        try:
            print("1.afisare")
            print("2.adaugare")
            print("3.stergere")
            print("4.save")
            print("5.load")
            print("6.ordonare")
            print("7.exit")
            opt=input("Optiunea aleasa este: ")
            if opt=="1":
                print(serv.print())
            elif opt=="2":
                id=input("id: ")
                model=input("model: ")
                maxpas=input("maxpas: ")
                avion=Avion(id,model,maxpas)
                serv.add_avi(avion)
            elif opt=="3":
                id=int(input("id: "))
                serv.delete(id)
            elif opt=="4":
                serv.save()
            elif opt=="5":
                serv.load()
            elif opt=="6":
                print(serv.ord())
            elif opt=="7":
                exit()
            else:
                print("Introduceti o comanda valida!!")

        except ValueError as eroare:
            print(eroare)