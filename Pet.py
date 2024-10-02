#! /usr/bin/python3

# from typing import Any # typing.Any vs object: 
# READ https://stackoverflow.com/questions/39817081/typing-any-vs-object

class Pet:

    # def __init__(self):
    #     print(self,": hola, mundo")

    def __init__(self, especie=None, nombre=None):
        self.__especie = especie
        self.nombre = nombre
        # print(self)

    # TODO: impedir el setting del nombre "666"
    # def __setattr__(self, name, value) -> None:
    #     if name == "__nombre":
    #         self.__nombre = value

    def __repr__(self):

        answ = f"<"
        answ += self.__especie
        answ +=f", "
        answ += self.nombre
        answ += f">"
        return answ


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

    # accesible? que?
    print(m2.nombre) 
    # print(m2.__especie)  # no alcanzable

    # m4 = Pet("Noche", "gato")  # error de uso
    m4 = Pet("gato", "Noche")    # el usuario debe saber .. o usar nombres
    m5 = Pet(especie="gato", nombre="Bamban")

    # setting
    m2.__setattr__("nombre", "Pompeta")
    print(m2)

    m2.__setattr__("__especie", "Pompeta")

    m666 = Pet(nombre="666")
    print(m666)


