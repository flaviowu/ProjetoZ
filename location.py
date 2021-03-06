from random import randint

class Market:               # lugar mercado, atribuímos valores nome e nome de item, além de uma quantidade aleatória de itens
    def __init__(self):
        self.name = "Mercado"
        self.item = "Comida"
        self.itemQ = randint(1, 2)

    def getName(self):
        return self.name

    def getItem(self):
        return self.item

    def getItemQ(self):
        return self.itemQ


class Hospital:
    def __init__(self):
        self.name = "Hospital"
        self.item = "Remédio"
        self.itemQ = randint(1, 2)

    def getName(self):
        return self.name

    def getItem(self):
        return self.item

    def getItemQ(self):
        return self.itemQ


class PoliceStation:
    def __init__(self):
        self.name = "Delegacia de Polícia"
        self.item = "Munição"
        self.itemQ = randint(1, 2)

    def getName(self):
        return self.name

    def getItem(self):
        return self.item

    def getItemQ(self):
        return self.itemQ


class Shelter:              # abrigo não tem ítens
    def __init__(self):
        self.name = "Abrigo"

    def getName(self):
        return self.name
