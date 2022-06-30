class Pokemon:

    def __init__(self, especie, level=1, nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({}) level {} ".format(self.especie, self.tipo, self.level)

    def atacar(self, pokemon):
        print("{} usou arranhar em {}!".format(self.especie, pokemon.especie))


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um choque do trovão em {}!".format(self.especie, pokemon.especie))


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou incendiar em {}!".format(self.especie, pokemon.especie))


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}!".format(self.especie, pokemon.especie))


class PokemonPlanta(Pokemon):
    tipo = "planta"

    def atacar(self, pokemon):
        print("{} usou chicote de vinhas em {}!".format(self.especie, pokemon.especie))