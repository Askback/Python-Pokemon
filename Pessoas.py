import Pokemon
from Pokemon import *


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Viajante"

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            for pokemon in self.pokemons:
                print("Pokemons de {}: {}".format(self, pokemon))
        else:
            print("{} não possuí pokemons".format(self))


class Player(Pessoa):
    tipo = "player"

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} Capturou um {} nivel {}!".format(self, pokemon.especie, pokemon.level))


class Inimigo(Pessoa):
    tipo = "Inimigo"


eu = Player(nome="kevin")
eu.mostrar_pokemons()

pokemon_wild = PokemonAgua("Squirtle")

eu.capturar_pokemon(pokemon_wild)
eu.mostrar_pokemons()


