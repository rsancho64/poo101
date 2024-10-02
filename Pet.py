# from typing import Any # typing.Any vs object: READ https://stackoverflow.com/questions/39817081/typing-any-vs-object

class Pet:

    # def __init__(self):
    #     print(self,": hola, mundo")

    def __init__(self, especie=None, nombre=None):
        self.__especie = especie
        self.nombre = nombre
        print(self)

    # def __setattr__(self, name, value) -> None:
    #     if name == "__nombre":
    #         self.__nombre = value

    # # TODO: vs __repr__? # SEE: https://jarroba.com/repr-y-str-de-python/
    def __str__(self) -> str:

        esp = self.__especie
        if not self.__especie: esp = "mascota"
        answ = f"soy un {esp}"

        if self.nombre:
            answ += f" y me llamo {self.nombre}"
        return answ

if __name__== "__main__":

    m0 = Pet()
    m1 = Pet(especie="perro")
    m2 = Pet(especie="perro", nombre="Pompa")
    m3 = Pet(nombre="Firulais",especie="perrete")

    print(m0)
    print(m1)
    print(m2)
    print(m3)

    print(m2.nombre) 
    # print(m2.__especie)  # no alcanzable

    # accesible? que? # TODO: test
    # print()

    # m2 = Pet("Noche") # TODO: MAKE IT CATS
    # m3 = Pet("Bamban")

    # TODO: 
    # m1.__setattr__("__nombre", "Pompeta")
    # print(m1)
