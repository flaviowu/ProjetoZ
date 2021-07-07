import personagens
import itens
import location
from random import randint, choice


def menu(listaOpcoes):
    opcoes = enumerate(listaOpcoes, 1)
    for i, v in opcoes:
        print(f"[{i}] - {v}")
    resposta = ""
    while resposta.isnumeric() == False:
        resposta = input("Escolha o número da opção\n-> ")
        while resposta.isnumeric() == True and int(resposta) not in list(range(1, len(listaOpcoes)+1)):
            resposta = input(
                "Escolha o número da opção dentre as do menu!\n-> ")
    return listaOpcoes[int(resposta) - 1]

def inOutAcao(lista, p):
    if p.getLocation().getName() != "Abrigo" and "Descansar" in lista :
        lista.remove("Descansar")
    elif personagem.getLocation().getName() == "Abrigo" and "Descansar" not in lista:
        lista.insert(len(lista)-3, "Descansar")
    else: pass

def inOutLugares(lista, p, destino):
    lista.remove(destino)
    if p.getLocation().getName() not in lista:
        lista.insert(2, p.getLocation().getName())
    lista.sort()


def luta(p):
    zumbi = personagens.Zombie()
    n = randint(1, 3)
    while n > 0:
        while zumbi.life > 0 and p.life > 0:
            iniciativa = randint(1)
            if iniciativa == 1:
                zumbi.attack(p)
            else:
                acao = menu(listaMenu["Ações de Luta"])
                if acao == "atacar":
                    arma = menu(listaMenu["Armas"])
                    p.attack(zumbi, arma)
                elif acao == "Fugir":
                    p.escape()
                    break

listaMenu = {"lugares": ["Mercado", "Hospital", "Delegacia de Polícia"],
                "Ações": ["Ir para outro lugar", "Comer", "Se medicar", "Recarregar pistola", "Olhar Mochila", "Sair"],
                "Ações de Luta": ["Atacar", "Fugir"],
                "Armas": ["Pistola", "Faca"]}
personagem = personagens.Survivor(100, 10)
lugar = location.Shelter()
while personagem.days > 0 or personagem.life > 0:
    print(personagem)
    inOutAcao(listaMenu["Ações"], personagem)
    acao = menu(listaMenu["Ações"])
    if acao == "Ir para outro lugar":
        destino = menu(listaMenu["lugares"])
        inOutLugares(listaMenu["lugares"], personagem, destino)
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
    elif acao == "Sair":
        break
    
    # 
    # elif acao == "Descansar":
    #     personagem.rest()
    # elif acao == "Recarregar Pistola":
    #     personagem.backpack.pistola.reload()
    


# zumbi = personagens.Zombie(50, 20)

