class Food:
    def __init__(self):
        self.value = 10
        self.quantity = 1

    def getValue(self):
        return self.value

    def getQuantity(self):
        return self.quantity

    def setQuantityUp(self, v):
        self.quantity += v

    def setQuantityDown(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.quantity = 0


class Medicine:
    def __init__(self):
        self.quantity = 1

    def getQuantity(self):
        return self.quantity

    def setQuantityUp(self, v):
        self.quantity += v

    def setQuantityDown(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.quantity = 0


class Ammo:
    def __init__(self):
        self.quantity = 1

    def getQuantity(self):
        return self.quantity

    def setQuantityUp(self):
        self.quantity += 1

    def setQuantityDown(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.quantity = 0


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

    def shot(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.dmg = 0
            self.quantity = 0


class Knife:
    def __init__(self):
        self.dmg = 1.1

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
        return f"Sua mochila tem:\n  Comida: {self.getComidaQ()} porções\n  Medicamentos: {self.getMedicineQ()} un\n  1 Faca\n  1 Pistola\n  Munição: {self.getAmmoQ()} caixas.\n"

    def getComidaQ(self):
        return self.comida.getQuantity()

    def getMedicineQ(self):
        return self.remedio.getQuantity()

    def getAmmoQ(self):
        return self.ammo.getQuantity()
