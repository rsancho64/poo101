from typing import Any

class Mascota:

    # def __init__(self):
    #     print(self,": hola, mundo")

    def __init__(self, nombre=None):
        self.__nombre = nombre
        # print(self, self.__nombre, ": hola")
        print(self.__nombre, ": hola")

    def __setattr__(self, name, value) -> None:
        if name == "__nombre":
            self.__nombre = value

    def __str__(self) -> str:
        return self.__nombre

if __name__== "__main__":

    m0 = Mascota()
    m1 = Mascota("Pompa")
    # print(m0 == m1)
    # print(m0.__nombre) #inaccesible
    # print(m1.__nombre) #inaccesible   

    m2 = Mascota("Noche")
    m3 = Mascota("Bamban")

    m1.__setattr__("__nombre", "Pompeta")
    print(m1)