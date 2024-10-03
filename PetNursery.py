#! /usr/bin/python3

from Pet import Pet


class PetNursery:

    def __init__(self):
        self.lista = []

    def addPet(self, aPet: Pet):
        self.lista.append(aPet)

    def __repr__(self) -> str:
        return str(self.lista)

    def __str__(self) -> str:

        # return self.__repr__()

        answ = f"{{"
        for pet in self.lista:
            answ += f"{pet}, "
        answ += f"}}"
        return answ


if __name__ == "__main__":

    p0 = Pet(especie="perro", nombre="Pompa")
    myPetNursery = PetNursery()
    print(myPetNursery.lista)
    print(myPetNursery)

    myPetNursery.addPet(p0)
    print(myPetNursery.lista)
    print(myPetNursery)

    p1 = Pet(especie="gato", nombre="Noche")
    myPetNursery.addPet(p1)
    print(myPetNursery.lista)
    print(myPetNursery)
