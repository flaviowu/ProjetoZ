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
                "Ações": ["Ir para outro lugar", "Comer", "Se medicar", "Descansar", "Recarregar pistola", "Olhar Mochila"],
                "Ações de Luta": ["Atacar", "Fugir"],
                "Armas": ["Pistola", "Faca"]}

personagem = personagens.Survivor(100, 10)
lugar = location.Shelter()
while personagem.days > 0 or personagem.life > 0:
    acao = menu(listaMenu["Ações"])
    if acao == "Ir para outro lugar":
        destino = menu(listaMenu["lugares"])
        listaMenu["lugares"].append(personagem.getLocation())
        listaMenu["lugares"].remove(destino)

        if destino == "Mercado":
            lugar = location.Market()
            personagem.setLocation(lugar)
            personagem.getItens(lugar.getItemQ())
        elif destino == "Hospital":
            lugar = location.Hospital()
            personagem.setLocation(lugar)
            personagem.getItens(lugar.getItemQ())
        elif destino == "Delegacia de Polícia":
            lugar = location.PoliceStation()
            personagem.setLocation(lugar)
            personagem.getItens(lugar.getItemQ())
        elif destino == "Abrigo":
            lugar = location.Shelter()
            personagem.setLocation(lugar)

        
    #     personagem.goTo()
    # elif acao == "Comer":
    #     personagem.eat()
    # elif acao == "Se medicar":
    #     personagem.getMed()
    # elif acao == "Descansar":
    #     personagem.rest()
    # elif acao == "Recarregar Pistola":
    #     personagem.backpack.pistola.reload()
    # elif acao == "Olhar Mochila":
    #     print(personagem.backpack)
    


# zumbi = personagens.Zombie(50, 20)
print(personagem)
print(personagem)

