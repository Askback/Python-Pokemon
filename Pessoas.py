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
        for pokemon in self.pokemons:
            print(pokemon)


class Player(Pessoa):
    tipo = "player"


class Inimigo(Pessoa):
    tipo = "Inimigo"


kevin_pokemon1 = PokemonFogo("Charmander", nome="José")
kevin_pokemon2 = PokemonEletrico("Stunkfish", nome="Dinaldo")

eu = Player(nome="kevin", pokemons=[kevin_pokemon1, kevin_pokemon2])


eu.mostrar_pokemons()
