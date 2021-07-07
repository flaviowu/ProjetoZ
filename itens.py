class Item:
    def __init__(self):
        self.name = ""
        self.value = 0
        self.quantity = 0
        self.Qmod = 1

    def getName(self):
        return self.name

    def setName(self):
        if self.quantity > 1:  # plural
            self.name = ""
        else:
            pass

    def getValue(self):
        return self.value * self.Qmod

    def getQuantity(self):
        return self.quantity

    def setQuantityUp(self, v):
        self.quantity += v

    def setQuantityDown(self):
        if self.quantity <= 0:
            self.quantity = 0
            self.Qmod = 0
        else:
            self.quantity -= 1
            self.Qmod = 1



class Food(Item):
    def __init__(self):
        super().__init__()
        self.name = "Comida"
        self.value = 10
        self.quantity = 1


class Medicine(Item):
    def __init__(self):
        super().__init__()
        self.name = "Cloropina"
        self.value = False
        self.quantity = 1


class Ammo(Item):
    def __init__(self):
        super().__init__()
        self.name = "Munição"
        self.quantity = 1


class Pistol:
    def __init__(self):
        self.dmg = 2
        self.bullet = 6

    def getBullet(self):
        return self.quantity

    def getDmg(self):
        return self.dmg

    def reload(self):
        self.quantity = 6
        Ammo.setQuantityDown(1)
        self.dmg = 2
        print(f"Você recarregou sua pistola.\nConsumiu 1 un de Munição e tem agora 6 balas no pente.")

    def shot(self):

        if self.quantity <= 0:
            self.dmg = 0
            self.quantity = 0
        else:
            self.quantity -= 1


class Knife:
    def __init__(self):
        self.dmg = 1.2

    def getDmg(self):
        return self.dmg


class BackPack:
    def __init__(self) -> None:
        self.comida = Food()
        self.remedio = Medicine()
        self.pistola = Pistol()
        self.faca = Knife()
        self.ammo = Ammo()

    def __str__(self):
        return f"Sua mochila tem:\n  Comida: {self.getComidaQ()} un\n  Medicamentos: {self.getMedicineQ()} un\n  1 Faca\n  1 Pistola\n  Munição: {self.getAmmoQ()} un\n"

    def getComidaQ(self):
        return self.comida.getQuantity()

    def getMedicineQ(self):
        return self.remedio.getQuantity()

    def getAmmoQ(self):
        return self.ammo.getQuantity()
