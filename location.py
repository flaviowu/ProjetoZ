from random import randint


class Market:
    def __init__(self):
        self.name = "Mercado"
        self.item = "Comida"
        self.itemQ = randint(1, 3)

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
        self.itemQ = randint(3)

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
        self.itemQ= randint(2)

    def getName(self):
        return self.name

    def getItem(self):
        return self.item

    def getItemQ(self):
        return self.itemQ

class Shelter:
    def __init__(self):
        self.name = "Abrigo"

    def getName(self):
        return self.name
