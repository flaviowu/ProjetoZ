import personagens
import location
import random

# função para printar qualquer menu recebendo uma lista, pedindo input da escolha e devolvendo uam str com a escolha
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

# tira a ação descansar se o personagem estiver fora do abrigo e coloca de volta se estiver de volta ao abrigo
def inOutAcao(lista, p):
    if p.getLocation().getName() != "Abrigo" and "Descansar" in lista:
        lista.remove("Descansar")
    elif personagem.getLocation().getName() == "Abrigo" and "Descansar" not in lista:
        lista.insert(len(lista)-3, "Descansar")
    else:
        pass

# tira da lista de opções de destino o lugar atual do personagem
def inOutLugares(lista, p, destino):
    lista.remove(destino)
    if p.getLocation().getName() not in lista:
        lista.insert(2, p.getLocation().getName())
    lista.sort()

# função script de luta: no caminho, o personagem encontra um número aleatório de zumbis com paramentros aleatórios.
def luta(p, d):
    zumbi = personagens.Zombie(random.choice(
        [20, 40, 60]), random.choice([20, 25, 30]))
    n = random.randint(1, 3)
    print(
        f"No caminho até o(a) {d}, você encontrou {n} zumbis! Se prepare para lutar pela sua vida!\n")
    while n > 0:
        n -= 1
        while zumbi.life > 0 and p.life > 0:
            # iniciativa = random.randint(1,20)
            p.getStatus()
            zumbi.getStatus()
            # if iniciativa >= 10:
            print("Um zumbi te atacou!\n")
            zumbi.attack(p)
            p.getStatus()
            #     print("=-"*25)
            # elif iniciativa < 10:
            acao = menu(listaMenu["Ações de Luta"])
            if acao == "Atacar":
                arma = menu(listaMenu["Armas"])
                p.attack(zumbi, arma)
            elif acao == "Fugir":
                p.escape()
                break

# dicionário de lista de lugares,, ações, ações durante a luta e armas. 
listaMenu = {"lugares": ["Mercado", "Hospital", "Delegacia de Polícia"],
             "Ações": ["Ir para outro lugar", "Comer", "Se medicar", "Recarregar Pistola", "Olhar Mochila", "Sair"],
             "Ações de Luta": ["Atacar", "Fugir"],
             "Armas": ["Pistola", "Faca"]}

# início do início
print(f"Recebemos sua mensagem e já triangulamos sua localização.\nFique tranquilo que o resgate chegará em TRÊS (3) dias.\nPara sua informação, nossos drones fazem depósitos frequentes de comida no Mercado, medicamentos no Hospital e munições na Delegacia de Polícia.\nSe precisar de algum suprimento, não hesite em buscá-los. Economize sua energia e descanse para recuperá-la,pois o local onde você se encontra é muito radioativo e portanto, sua vida pode se esgotar rapidamente.\nSobreviva!")
start = ""
mainFlag = True
runFlag = 0
# loop de opções de inicio
while mainFlag:
    start = input("Deseja iniciar? (S/N)").upper()
    if start == "S":
        runFlag = True
        mainFlag = False
    elif start == "N":
        runFlag = False
        mainFlag = False
    elif start != "S" or start != "N":
        continue

# início do loop in Game
personagem = personagens.Survivor(100, 10)  # instacioação do personagem
lugar = location.Shelter()                  # instanciação do lugar inicial = Abrigo
while personagem.getDia() > 0 and personagem.getLife() > 0 and runFlag == True:
    personagem.getStatus()
    inOutAcao(listaMenu["Ações"], personagem)
    acao = menu(listaMenu["Ações"])                 # pede função menu principal de ações
    if acao == "Ir para outro lugar":               # ação Ir para outro lugar
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

if personagem.getDia() == 0:
    print(f"TUDUDUDUDUDUDUDUDUDUDUDU\nVocê avistou um helicóptero e correu em direção a ele.\nO barulho das hélices do helicóptero atraiu uma horda de zumbis!!\nQuando você se aproximava do helicóptero, um soldado jogou uma escada de corda e você subiu por ela e foi RESGATADO!\nParabéns, você sobreviveu ao apocalipse por enquanto, mas a aventura está só começando.")
elif personagem.getLife() == 0:
    print(f"Infelizmente, você não sobreviveu até a equipe de resgate chegar.\nGAME OVER.")
elif (personagem.getDia() > 0 and personagem.getLife() > 0) or runFlag ==False:
    print(f"Volte mais vezes!")


# print(personagem)
# print(personagem.backpack)
# personagem.reloadGun()
# print(personagem)
# print(personagem.backpack)


# zumbi = personagens.Zombie(50, 20)
