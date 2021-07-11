from random import choice
import itens
import location


class Human:                                # classe Human para personagem genérico
    def __init__(self, life=100, dmg=1):
        self.life = life
        self.lifeMax = 100
        self.alive = True
        self.infected = False
        self.dmg = dmg

    def __str__(self):
        return f"Vida {self.life}, Infecção: {self.infected}"

    def getLife(self):
        return self.life

    def isAlive(self):
        return self.alive

    def isInfected(self):
        return self.infected

    def getDmg(self):
        return self.dmg

    def lifeUp(self, up):
        if self.life <= 90:
            self.life = self.lifeMax
        elif 90 > self.life <= 100:
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


class Survivor(Human):                  # subclasse Human que herda parametros e funções de Human
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.location = location.Shelter()
        self.energy = 3
        self.days = 3
        self.backpack = itens.BackPack()

    def getStatus(self):  # printa status do personagem
        print("-=-"*10)
        print(
            f"Faltam {self.getDia()} {'dia' if self.getDia == 1 else 'dias'} para o resgate.")
        print("> Player Status:")
        print(f"{'> Vida': <15}{self.life}")
        print(
            f"{'> Infecção': <15}{'Saudável' if self.infected == False else 'Infectado'}")
        print(f"{'> Pistola': <15}{self.backpack.pistola.getBullet()} Bala(s)")
        print(f"{'> Local Atual': <15}{self.getLocation().getName()}")
        print("-=-"*10)

    def setLocation(self, newLocation):
        self.location = newLocation

    def getLocation(self):
        return self.location

    def getEnergy(self):
        return self.energy

    def setEnergyUp(self):
        self.energy = 3

    def setEnergyDown(self):
        if self.getEnergy() <= 0:
            self.lifeDown(10)
        else:
            self.energy -= 1

    def eat(self, v):
        if self.backpack.comida.getQuantity() > 0:
            oldLife = self.getLife()
            self.lifeUp(v)
            self.backpack.comida.setQuantityDown()
            print(
                f"Você comeu 1 un de comida e sua vida subiu em {self.getLife()-oldLife}\n")
        else:
            print(f"Você não tem mais comida. Tente procurar em um mercado.\n")

    def getMedicine(self):
        if self.backpack.remedio.getQuantity() > 0:
            self.setNonInfected()
            self.backpack.remedio.setQuantityDown()
            print(f"Você tomou uma dose de Cloropina e deteve a infecção.\n")
        else:
            print(f"Você tomou não tem mais doses de Cloropina.\n")

    def attack(self, enemy, weapon):
        oldLife = enemy.getLife()
        if weapon == "Faca":
            dmgMod = self.backpack.faca.getDmg()
        elif weapon == "Pistola":
            dmgMod = self.backpack.pistola.getDmg()
            print(f"Você pegou sua arma, apontou para o zumbi e puxou o gatilho.\n")
            self.backpack.pistola.shot()
        enemy.lifeDown(self.getDmg() * dmgMod)
        newLife = enemy.getLife()
        print(f"O zumbi perdeu {oldLife - newLife} pontos de vida\n")

    def reloadGun(self):
        if self.backpack.ammo.getQuantity() > 0:
            self.backpack.ammo.setQuantityDown()
            self.backpack.pistola.reload()
            print(
                f"Você pegou uma caixa de Munições e recarregou a pistola. Você tem agora {self.backpack.pistola.getBullet()} balas no pente.\n")

        else:
            print(f"Você revirou a mochila procurando pela sua munição, mas não achou nada. Talvez vc deva dar uma procurada na Delegacia de Polícia\n")

    def goTo(self, newLocation):
        if self.energy > 0:
            self.setEnergyDown()
            self.setLocation(newLocation)
            print(f"Você chegou ao seu destino e gastou 1 ponto de energia.\n")
        else:
            self.setEnergyDown()
            print(
                f"Você não tem energia para se locomover. Ao invés de gastar energia, você gastou 10 de vida\n")

    def pickUpItens(self, qtd):
        if self.location.getName() == "Mercado":
            self.backpack.comida.setQuantityUp(qtd)
            print(f"Você encontrou {qtd} und de comida.\n")
        elif self.location.getName() == "Hospital":
            self.backpack.remedio.setQuantityUp(qtd)
            print(f"Você encontrou {qtd} und de Cloropina.\n")
        elif self.location.getName() == "Delegacia de Polícia":
            self.backpack.ammo.setQuantityUp(qtd)
            print(f"Você encontrou {qtd} caixa(s) de munição.\n")

    def escape(self):
        self.setEnergyDown()

    def passaDia(self):
        self.days -= 1

    def getDia(self):
        return self.days

    def rest(self):
        self.setEnergyUp()
        oldLife = self.getLife()
        self.passaDia()
        self.lifeDown(choice([30, 40, 50]))
        print(
            f"Você dormiu a acordou no dia seguinte.\nRecuperou energia máxima (3 pontos), porém, devido à radiação, você perdeu {oldLife - self.getLife()} pontos de vida.\n")


class Zombie(Human):                # classe zumbi derivada de human
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.life = life
        self.dmg = dmg
        self.alive = False

    def getStatus(self):
        print("-=-"*10)
        print("> Zombie Status:")
        print(f"{'> Vida': <15}{self.life}")
        print("-=-"*10)

    def attack(self, enemy):
        oldLife = enemy.getLife()
        enemy.lifeDown(self.dmg)
        print(
            f"Você foi atacado pelo zumbi e perdeu {oldLife - enemy.getLife()} pontos de vida.\n")
        if enemy.isInfected == False and choice([True, False]) == True:
            enemy.setInfected()
            print("Você foi infectado! Tome uma dose de Cloropina assim que possível.\n")
