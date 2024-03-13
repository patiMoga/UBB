class Avion:
    def __init__(self,id,model,maxpas):

        try:
            id=int(id)
        except:
            raise ValueError("ID nu este numar")

        if id<0:
            raise ValueError("ID este negativ")
        self.id=id
        if len(model)!=5:
            raise ValueError("Model gresit!!!!!")
        if model[0] in "1234567890" or model[1] in "1234567890" or model[0]!=model[0].upper() or model[1]!=model[1].upper():
            raise ValueError("Model gresit!!!!!")
        if model[2] not in "1234567890" or model[3] not in "1234567890" or model[4] not in "1234567890":
            raise ValueError("Model gresit!!!!!")
        self.model=model
        try:
            maxpas = int(maxpas)
        except:
            raise ValueError("maxim pasageri nu este numar")

        if maxpas < 0:
            raise ValueError("maxim pasageri este negativ")
        self.maxpas=maxpas

    def __str__(self):
        return "id: "+str(self.id)+ " model: "+self.model+" maxpas: "+str(self.maxpas)