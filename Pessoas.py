import random
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

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

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
        pessoa.mostrar_pokemons()

        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon_aliado = self.escolher_pokemon()

        if pokemon_aliado and pokemon_inimigo:
            while True:
                if pokemon_aliado.atacar(pokemon_inimigo):
                    print("\n{} ganhou a batalha ( ͡ᵔ ͜ʖ ͡ᵔ)".format(self))
                    break
                if pokemon_inimigo.atacar(pokemon_aliado):
                    print("\n{} ganhou a batalha ( ͡ᵔ ͜ʖ ͡ᵔ)".format(pessoa))
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
                except:
                    print("Escolha inválida")
        else:
            print("Esse jogador não possuí pokemons disponiveis (╥︣﹏᷅╥)\n")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)
