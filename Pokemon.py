import random


class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.pontos_ataque = self.level * 1.25
        self.pontos_vida = self.level * 3

    def __str__(self):
        return "{} level {} ".format(self.especie, self.level)

    def atacar(self, pokemon):
        pokemon.pontos_vida = pokemon.pontos_vida - (self.pontos_ataque * random.uniform(self.level, 3))
        print("{} perdeu {:.1f} pontos de vida\n".format(pokemon, self.pontos_ataque * random.uniform(self.level, 3)))

        if pokemon.pontos_vida <= 0:
            print("{} Foi derrotado".format(pokemon))
            print("\n------------------------------------")
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um choque do trovão em {}!\n".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou incendiar em {}!\n".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}!\n".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)


class PokemonPlanta(Pokemon):
    tipo = "planta"

    def atacar(self, pokemon):
        print("{} usou chicote de vinhas em {}!\n".format(self.especie, pokemon.especie))
        return super().atacar(pokemon)

