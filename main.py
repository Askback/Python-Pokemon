import time

from Pessoas import *
from Pokemon import *


def escolha_inicial(player):
    print("Olá {} esse é o momento mais importante de sua jornada".format(player))
    print("Seu pokemon inicial deverá lhe acompanhar pela sua trajetória")

    bulbasaur = PokemonPlanta("Bulbasaur", level=1,)
    charmander = PokemonFogo("Charmander", level=1,)
    squirtle = PokemonAgua("Squirtle", level=1,)

    print("Será um dessas três opções")
    print("1- ", charmander)
    print("2- ", bulbasaur)
    print("3- ", squirtle)

    while True:
        escolha = input("Digite o número referente ao pokemon: ")

        if escolha == "1":
            player.capturar_pokemon(charmander)
            break
        elif escolha == "2":
            player.capturar_pokemon(bulbasaur)
            break
        elif escolha == "3":
            player.capturar_pokemon(squirtle)
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    print("---------------------------------------------")
    print("Bem vindo ao Projeto de Pokemon via Terminal")
    print("---------------------------------------------")
    nome = input("\nDigite seu nome para nos conhecermos melhor: ")
    player = Player(nome)
    print("\nEntendi você é o {}, pronto para sua aventura? Espero que sim!".format(player))

    if player.pokemons:
        print("\nJá conheço seus pokemons: ")
        player.mostrar_pokemons()
    else:
        print("\nNão encontrei nenhum pokemon com você, deve escolher um !")
        escolha_inicial(player)
        print("\nExcelente escolha! o {} será perfeito...".format(player.pokemons[0]))
        print("\nQue tal já testar seu novo amigo em combate? Gary vem logo ai")
        print("---------------------------------------------")
        gary = Inimigo(nome="Gary", pokemons=[PokemonPlanta("Bulbasaur", level=1)])
        player.batalhar(gary)

    while True:
        print("---------------------------------------------")
        print("O que deseja fazer agora?: ")
        print("\n1 - Explorar o mundo")
        print("\n2 - Batalha randomica")
        print("\n3 - Meus pokemons")
        print("\n4 - Meu saldo")
        print("\n5 - Sair do jogo")
        print("---------------------------------------------")
        escolha = input()

        if escolha == '5':
            print("\nAté logo amigo...... (y)")
            exit()
        elif escolha == '1':
            player.explorar()
        elif escolha == '2':
            random_inimigo = Inimigo()
            player.batalhar(random_inimigo)
        elif escolha == '3':
            player.mostrar_pokemons()
            time.sleep(2)
        elif escolha == '4':
            player.mostrar_dinheiro()
            time.sleep(2)
        else:
            print("\nEscolha inválida")
