from Pokemon import *
from Pessoas import *


def escolha_inicial(player):
    print("Olá {} esse é o momento mais importante de sua jornada".format(player))
    print("Seu pokemon inicial deverá lhe acompanhar pela sua trajetória")

    bulbasaur = PokemonPlanta("Bulbasaur", level=1,)
    charmander = PokemonFogo("Charmander", level=1,)
    squitle = PokemonAgua("Squirtle", level=1,)

    print("Será um dessas três opções")
    print("1- ", charmander)
    print("2- ", bulbasaur)
    print("3- ", squitle)

    while True:
        escolha = input("Digite o número referente ao pokemon: ")

        if escolha == "1":
            player.capturar_pokemon(charmander)
            break
        elif escolha == "2":
            player.capturar_pokemon(bulbasaur)
            break
        elif escolha == "3":
            player.capturar_pokemon(squitle)
            break
        else:
            print("Opção inválida")


eu = Player(nome="Kevao", pokemons=[PokemonAgua("Squirtle", level=1)])

gary = Inimigo(nome="Gary", pokemons=[PokemonPlanta("Bulbasaur", level=1)])

eu.batalhar(gary)
