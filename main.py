import personagens
import location
import random
'''
Recebemos sua mensagem e já triangulamos sua localização.
Fique tranquilo que o resgate chegará em TRÊS (3) dias. Para sua informação, nossos drones fazem depósitos frequentes de comida no Mercado,
medicamentos no Hospital e munições na Delegacia de Polícia. Se precisar de algum suprimento, não hesite em buscá-los. Economize sua energia e descanse para recuperá-la,
pois o local onde
você se encontra é muito radioativo e portanto, sua vida pode se esgotar rapidamente.
Sobreviva!
'''

'''
Infelizmente, você não sobreviveu até nossa equipe de resgate chegar.
GAME OVER
'''

'''
TUDUDUDUDUDUDUDUDUDUDUDU
Você avistou um helicóptero e correu em direção a ele.
O barulho das hélices do helicóptero atraiu uma horda de zumbis!
Quando você se aproximava do helicóptero, um soldado jogou uma escada de corda...
'''


def menu(listaOpcoes):
    print("-=-=-=-=-=-= Menu =-=-=-=-=-=-")
    opcoes = enumerate(listaOpcoes, 1)
    for i, v in opcoes:
        print(f"[{i}] - {v}")
    resposta = ""
    while resposta.isnumeric() == False:
        print("-=-"*10)
        resposta = input("Escolha o número da opção\n-> ")
        while resposta.isnumeric() == True and int(resposta) not in list(range(1, len(listaOpcoes)+1)):
            resposta = input(
                "Escolha o número da opção dentre as do menu!\n-> ")
    return listaOpcoes[int(resposta) - 1]


def inOutAcao(lista, p):
    if p.getLocation().getName() != "Abrigo" and "Descansar" in lista:
        lista.remove("Descansar")
    elif personagem.getLocation().getName() == "Abrigo" and "Descansar" not in lista:
        lista.insert(len(lista)-3, "Descansar")
    else:
        pass


def inOutLugares(lista, p, destino):
    lista.remove(destino)
    if p.getLocation().getName() not in lista:
        lista.insert(2, p.getLocation().getName())
    lista.sort()


def luta(p, d):
    zumbi = personagens.Zombie(random.choice([20, 40, 60]), random.choice([1, 5, 10]))
    n = random.randint(1, 3)
    print(f"No caminho até o(a) {d}, você encontrou {n} zumbis! Se prepare para lutar pela sua vida!\n")
    while n > 0:
        n -= 1
        while zumbi.life > 0 and p.life > 0:
            # iniciativa = random.randint(1,20)
            p.getStatus()
            zumbi.getStatus()
            # if iniciativa >= 10:
            print("Um zumbi te atacou!")
            zumbi.attack(p)
            #     print("=-"*25)
            # elif iniciativa < 10:
            acao = menu(listaMenu["Ações de Luta"])
            if acao == "Atacar":
                arma = menu(listaMenu["Armas"])
                p.attack(zumbi, arma)
            elif acao == "Fugir":
                p.escape()
                break
          

listaMenu = {"lugares": ["Mercado", "Hospital", "Delegacia de Polícia"],
             "Ações": ["Ir para outro lugar", "Comer", "Se medicar", "Recarregar Pistola", "Olhar Mochila", "Sair"],
             "Ações de Luta": ["Atacar", "Fugir"],
             "Armas": ["Pistola", "Faca"]}
personagem = personagens.Survivor(100, 10)
lugar = location.Shelter()
while personagem.days > 0 or personagem.life > 0:
    personagem.getStatus()
    inOutAcao(listaMenu["Ações"], personagem)
    acao = menu(listaMenu["Ações"])
    if acao == "Ir para outro lugar":
        destino = menu(listaMenu["lugares"])
        inOutLugares(listaMenu["lugares"], personagem, destino)
        luta(personagem, destino)
        if destino == "Mercado":
            lugar = location.Market()
            personagem.goTo(lugar)
            personagem.pickUpItens(lugar.getItemQ())
        elif destino == "Hospital":
            lugar = location.Hospital()
            personagem.goTo(lugar)
            personagem.setLocation(lugar)
            personagem.pickUpItens(lugar.getItemQ())
        elif destino == "Delegacia de Polícia":
            lugar = location.PoliceStation()
            personagem.goTo(lugar)
            personagem.setLocation(lugar)
            personagem.pickUpItens(lugar.getItemQ())
        elif destino == "Abrigo":
            lugar = location.Shelter()
            personagem.goTo(lugar)
            personagem.setLocation(lugar)
    elif acao == "Comer":
        personagem.eat(personagem.backpack.comida.getValue())
    elif acao == "Se medicar":
        personagem.getMedicine()
    elif acao == "Olhar Mochila":
        print(personagem.backpack)
    elif acao == "Descansar":
        personagem.rest()
    elif acao == "Recarregar Pistola":
        personagem.reloadGun()
    elif acao == "Sair":
        break


# print(personagem)
# print(personagem.backpack)
# personagem.reloadGun()
# print(personagem)
# print(personagem.backpack)



# zumbi = personagens.Zombie(50, 20)
