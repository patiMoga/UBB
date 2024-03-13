class Masina:
    def __init__(self, marca, model, tokenMasina,pretVanzare, pretAchizitie):
        self.marca = marca
        self.model = model
        self.tokenMasina = tokenMasina
        self.pretVanzare = pretVanzare
        self.pretAchizitie = pretAchizitie

    def returnare(self, comparator):
        if(comparator == 'marca'):
            return self.marca
        elif(comparator == 'model'):
            return self.model
        elif(comparator == 'tokenMasina'):
            return self.tokenMasina
        elif(comparator == 'pretAchizitie'):
            return self.pretAchizitie
        elif(comparator == 'pretVanzare'):
            return self. pretVanzare
        else:
            return -1


