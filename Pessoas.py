import random
import time

from Pokemon import *

NOMES = [
    "Jota", "Silva", "Perono", "Paritza", "Bicardo", "Loreno", "Lutoco", "LindaLinda"
]

POKEMONS = [
    PokemonFogo("Infernape"),
    PokemonFogo("Rapidash"),
    PokemonFogo("Tepig"),
    PokemonAgua("Lapras"),
    PokemonAgua("Vaporeon"),
    PokemonAgua("Wailord"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Electrabuzz"),
    PokemonEletrico("Voltorb"),
    PokemonPlanta("Bulbasaur"),
    PokemonPlanta("Rilaboom"),
    PokemonPlanta("Shaymin")
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            for index, pokemon in enumerate(self.pokemons):
                print("Pokemons de {}: {}- {}\n".format(self, index, pokemon))
        else:
            print("{} não possuí pokemons (╥︣﹏᷅╥)\n".format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}\n".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Erro não {} possui nenhum pokemon (╥︣﹏᷅╥)\n".format(self))

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {} (ง︡'-'︠)ง\n".format(self, pessoa))
        print(" -------------------------------------")
        pessoa.mostrar_pokemons()
        print(" --#--#--#--#--#--#--#--#--#--#--#")

        pokemon_aliado = self.escolher_pokemon()
        pokemon_inimigo = pessoa.escolher_pokemon()
        time.sleep(1)
        print("\nA batalha começa em 3")
        time.sleep(1)
        print("\n2")
        time.sleep(1)
        print("\n1")
        time.sleep(1)

        if pokemon_aliado and pokemon_inimigo:
            while True:
                if pokemon_aliado.atacar(pokemon_inimigo):
                    print("\n{} ganhou a batalha ( ͡ᵔ ͜ʖ ͡ᵔ)".format(self))
                    self.ganhar_dinheiro(random.randint(1, 3) * pokemon_inimigo.level)
                    break
                if pokemon_inimigo.atacar(pokemon_aliado):
                    print("\n{} ganhou a batalha ( ͡ᵔ ͜ʖ ͡ᵔ)".format(pessoa))
                    self.perder_dinheiro(random.randint(1, 3) * pokemon_inimigo.level)
                    break
        else:
            print("Essa batalha não pode ocorrer")


class Player(Pessoa):
    tipo = "player"

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} Capturou um {} nivel {} ٩(˘◡˘)۶!\n".format(self, pokemon.especie, pokemon.level))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha com qual pokemon desejar batalhar: ")
                escolha = int(escolha)
                try:
                    pokemon_escolhido = self.pokemons[escolha]
                    print("-----------------------------\n")
                    print("\n{} eu escolho você\n".format(pokemon_escolhido))
                    print("-----------------------------\n")
                    return pokemon_escolhido
                except Exception as e:
                    print("Erro não foi possivel localizar este pokemon",e)
        else:
            print("Esse jogador não possuí pokemons disponiveis (╥︣﹏᷅╥)\n")

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro = self.dinheiro + quantidade
        print("\nVocê ganhou {} coins".format(quantidade))
        self.mostrar_dinheiro()

    def perder_dinheiro(self, quantidade):
        self.dinheiro = self.dinheiro - quantidade
        print("\nVocê perdeu {} coins".format(quantidade))
        self.mostrar_dinheiro()

    def mostrar_dinheiro(self):
        print("\nVocê possui atualmente {} coins".format(self.dinheiro))

    def explorar(self):
        if random.random() >= 0.5:
            pokemon = random.choice(POKEMONS)
            while True:
                decisao = input("\nUm {} selvagem apareceu, deseja tentar capturar? s/n: ".format(pokemon))
                if decisao == 's':
                    if random.random() >= 0.5:
                        self.capturar_pokemon(pokemon)
                        break
                    else:
                        print("\nO pokemon escapou =(")
                        break
                elif decisao == 'n':
                    print("\nBoa viagem, continue em frente")
                    break
                else:
                    print("\nOpção inválida, escolha entre s/n")

        elif random.random() >= 0.9:
            inimigo = Inimigo()
            while True:
                decisao = input("\nO treinador {} te desafiou, deseja enfrenta-lo? s/n: ".format(inimigo))
                if decisao == 's':
                    self.batalhar(inimigo)
                    break
                elif decisao == 'n':
                    print("\n Lembre-se, não da para fugir para sempre!")
                    break
                else:
                    print("\nOpção inválida, escolha entre s/n")
        else:
            print("\n A exploração não deu em nada :(")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)
