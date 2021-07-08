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


class Survivor(Human):
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.location = location.Shelter()
        self.energy = 3
        self.days = 3
        self.backpack = itens.BackPack()

    def getStatus(self):
        print("-=-"*10)
        print("> Player Status:")
        print(f"{'> Vida': <15}{self.life}")
        print(f"{'> Infecção': <15}{'Saudável' if self.infected == False else 'Infectado'}")
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
        else: self.energy -= 1

    def eat(self, v):
        if self.backpack.comida.getQuantity() > 0:
            oldLife = self.getLife()
            self.lifeUp(v)
            self.backpack.comida.setQuantityDown()
            print(
                f"Você comeu 1 un de comida e sua vida subiu em {self.getLife()-oldLife}")
        else:
            print("Você não tem mais comida. Tente procurar em um mercado.")

    def getMedicine(self):
        if self.backpack.remedio.getQuantity() > 0:
            self.setNonInfected()
            self.backpack.remedio.setQuantityDown()
            print("Você tomou uma dose de Cloropina e deteve a infecção.")
        else:
            print(f"Você tomou não tem mais doses de Cloropina.")

    def attack(self, enemy, weapon):
        if weapon == "Faca":
            dmgMod = self.backpack.faca.getDmg()
        elif weapon == "Pistola":
            dmgMod = self.backpack.pistola.getDmg()
            print("Você pegou sua arma, apontou para o zumbi e puxou o gatilho.")
            self.backpack.pistola.shot()
        enemy.lifeDown(self.dmg * dmgMod)

    def reloadGun(self):
        if self.backpack.ammo.getQuantity() > 0:
            print(f"Você pegou uma caixa de Munições e recarregou a pistola. Você tem agora {self.backpack.pistola.getBullet()} balas no pente.")
            self.backpack.ammo.setQuantityDown()
            self.backpack.pistola.reload()
        else: print("Você revirou a mochila procurando pela sua munição, mas não achou nada.")

    def goTo(self, newLocation):
        if self.energy > 0:
            self.setEnergyDown()
            self.setLocation(newLocation)
            print(f"Você chegou ao seu destino e gastou 1 ponto de energia.")
        else:
            self.setEnergyDown()
            print(
                "Você não tem energia para se locomover. Ao invés de gastar energia, você gastou 10 de vida")

    def pickUpItens(self, qtd):
        if self.location.getName() == "Mercado":
            self.backpack.comida.setQuantityUp(qtd)
            print(f"Você encontrou {qtd} un de comida.")
        elif self.location.getName() == "Hospital":
            self.backpack.remedio.setQuantityUp(qtd)
            print(f"Você encontrou {qtd} un de Cloropina.")
        elif self.location.getName() == "Delegacia de Polícia":
            self.backpack.ammo.setQuantityUp(qtd)
            print(f"Você encontrou {qtd} caixa(s) de munição.")

    def escape(self):
        self.setEnergyDown()

    def rest(self):
        self.setEnergyUp()
        oldLife = self.getLife()
        self.lifeDown(choice([10, 20]))
        print(f"Você dormiu por 8h e recuperou energia máxima (3 pontos), porém, devido à radiação, você perdeu {oldLife - self.getLife()}.")


class Zombie(Human):
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
        enemy.lifeDown(self.dmg)
        if choice([True, False]) == True:
            enemy.setInfected()


# personagem = Survivor(100, 10)
# personagem.getStatus()
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
