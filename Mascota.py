# from typing import Any

class Mascota:

    # def __init__(self):
    #     print(self,": hola, mundo")

    def __init__(self, especie="animal", nombre=None):
        self.__especie = especie
        self.nombre = nombre
        print(f"soy un {self.__especie} y me llamo {self.nombre}")  # TODO: USE self__str__?

    # def __setattr__(self, name, value) -> None:
    #     if name == "__nombre":
    #         self.__nombre = value

    # # TODO: vs __repr__? # SEE: https://jarroba.com/repr-y-str-de-python/
    # def __str__(self) -> str: 
    #     return "{0}".format(self.__nombre)

if __name__== "__main__":

    m0 = Mascota()
    m1 = Mascota(especie="perro")
    m3 = Mascota(especie="perro", nombre="Pompa")
    m4 = Mascota(nombre="Firulais",especie="perrete")
    
    # accesible? que? # TODO: test
    # print()

    # m2 = Mascota("Noche") # TODO: MAKE IT CATS
    # m3 = Mascota("Bamban")

    # TODO: 
    # m1.__setattr__("__nombre", "Pompeta")
    # print(m1)