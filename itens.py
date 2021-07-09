class Item:             # classe item genérico
    def __init__(self):
        self.name = ""
        self.value = 0
        self.quantity = 0

    def getName(self):
        return self.name

    def setName(self):
        if self.quantity > 1:
            self.name = ""
        else:
            pass

    def getValue(self):
        return self.value

    def getQuantity(self):
        return self.quantity

    def setQuantityUp(self, v):
        self.quantity += v

    def setQuantityDown(self):
        if self.quantity <= 0:
            pass
        else:
            self.quantity -= 1


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
        self.name = "Pistola"
        self.dmg = 2
        self.bullet = 1

    def getBullet(self):
        return self.bullet

    def setBulletDown(self):
        if self.getBullet() <= 0:
            pass
        else:
            self.bullet -= 1

    def setBulletUp(self):
        self.bullet = 6

    def getDmg(self):
        return self.dmg

    def setDmg(self, v):
        self.dmg = v

    def reload(self):
        self.setBulletUp()
        self.setDmg(2)

    def shot(self):
        if self.getBullet() <= 0:
            self.setDmg(0)
            print(f"Quando você puxou o gatilho, nada aconteceu.\n")
            print(f"Você não tem mais balas.\n")
        else:
            self.setDmg(2)
            self.setBulletDown()


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
        return f"Sua mochila tem:\n  Comida: {self.comida.getQuantity()} un\n  Medicamentos: {self.remedio.getQuantity()} un\n  1 Faca\n  1 Pistola\n  Munição: {self.ammo.getQuantity()} und\n"

# municao = Ammo()
# pistola = Pistol()
# print(f"munição {municao.getQuantity()}")
# municao.setQuantityDown()
# print(f"Balas: {pistola.getBullet()}")
# print(f"muniçao {municao.getQuantity()}")
# pistola.shot()
# print(f"Balas: {pistola.getBullet()}")
# pistola.shot()
# print(f"Balas: {pistola.getBullet()}")
# pistola.reload()
# print(f"Balas: {pistola.getBullet()}")
