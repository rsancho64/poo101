#! /usr/bin/python3

from typing import Any  ## automagicamente !?
# TODO READ https://stackoverflow.com/questions/39817081/typing-any-vs-object

class Pet:

    nombre = None  # class var declared (,, static) Not protected.

    def __init__(self, especie=None, nombre=None):
        self.__especie = especie  # __XXX notation: protected
        self.nombre = nombre      # wo class var declaration ,, Nones lost
        # print(f"init: {self.__especie},{self.nombre}")
        # print(self.__repr__())

    # TODO: impedir el setting del nombre "666"
    def __setattr__(self, name, value):
        if value=="666":
            print("oops: 666 forbidden!")
        else:
            super(Pet, self).__setattr__(name, value)

    def __repr__(self):

        answ = f"<"
        answ += str(self.__especie)  # new : cast to str
        answ +=f", "
        answ += str(self.nombre)     # new : cast to str
        answ += f">"
        return answ

    # TODO: vs __repr__? # SEE: https://jarroba.com/repr-y-str-de-python/
    def __str__(self) -> str:

        esp = self.__especie
        if not self.__especie: esp = "mascota"
        answ = f"soy un {esp}"

        nom = self.nombre
        if self.nombre:
            answ += f" y me llamo {nom}"
        
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

    mXXX = Pet(nombre="999")
    print(mXXX)

    mXXX.__setattr__("nombre", "333")
    print(mXXX)

    mXXX.__setattr__("nombre", "666")
    print(mXXX)

    mXXX.nombre = "111"  # desprotegida pero con __settattr__() programado
    print(mXXX)

    mXXX.nombre = "666"  # desprotegida pero con __settattr__() programado
    print(mXXX)
