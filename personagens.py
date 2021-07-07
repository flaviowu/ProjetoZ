from random import choice
import itens
import location


class Human:
    def __init__(self, life=100, dmg=1):
        self.life = life
        self.lifeMax = 100
        self.alive = True
        self.infected = False
        self.dmg = dmg

    def __str__(self):
        return f"Vida {self.life}, {self.infected}"

    def getLife(self):
        return self.life

    def isAlive(self):
        return self.alive

    def isInfected(self):
        return self.infected

    def getDmg(self):
        return self.dmg

    def lifeUp(self, up):
        self.life += up

    def lifeDown(self, down):
        self.life -= down
        if self.life <= 0:
            self.dead()
            self.life = 0

    def setInfected(self):
        self.infected = True
        self.dmg

    def setNonInfected(self):
        self.infected = False

    def dead(self):
        self.alive = False


class Survivor(Human):
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.location = location.Shelter()
        self.energy = 2
        self.days = 3
        self.backpack = itens.BackPack()

    def setLocation(self, newLocation):
        self.location = newLocation

    def getLocation(self):
        return self.location

    def setEnergy(self, v):
        self.energy += v

    def eat(self, v):
        self.lifeUp(v)

    def getMed(self):
        self.setNonInfected()
        itens.Medicine.quantity

    def attack(self, enemy, weapon):
        if weapon == "Faca":
            dmgMod = self.backpack.faca.getDmg()
        elif weapon == "Pistola":
            dmgMod = self.backpack.pistola.getDmg()
        enemy.lifeDown(self.dmg * dmgMod)

    def goTo(self, newLocation):
        if self.energy > 0:
            self.setEnergy(-1)
            self.location(newLocation.getName())
        else:
            print(
                "Você não tem energia para se locomover. Ao invés de gastar energia, você gastou 10 de vida")

    def getItens(self, qtd):
        if self.location.getName() == "Mercado":
            self.backpack.comida.setQuantityUp(qtd)
        elif self.location.getName() == "Hospital":
            self.backpack.remedio.setQuantityUp(qtd)
        elif self.location.getName() == "Delegacia de Polícia":
            self.backpack.ammo.setQuantityUp(qtd)
    
    def escape(self):
        self.setEnergy(-1)

    def rest(self):
        self.setEnergy(2)


class Zombie(Human):
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.life = life
        self.dmg = dmg
        self.alive = False

    def attack(self, enemy):
        enemy.lifeDown(self.dmg)
        if choice([True, False]) == True:
            enemy.setInfected()


# personagem = Survivor(100, 10)
# zumbi = Zombie(50, 20)
# i = 0
# while personagem.isAlive() == True:
#     i += 1
#     print(f"Você foi atacado {i}x")
#     zumbi.attack(personagem)
#     personagem.attack(zumbi)
#     print(f"Você: {personagem}")
#     print(f"Zumbi: {zumbi}")
#     print("--==")
