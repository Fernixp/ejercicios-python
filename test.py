class Animal:
    def __init__(self, nombre, raza):
        self.nombre  = nombre
        self.raza = raza


nombre = input("Ingrese el nombre\n")
raza = input("ingrese la raza del animalito\n")

animal = Animal(nombre, raza)

print("El animal Ingresado es:\n")
print(f"Nombre: {animal.nombre}")
print(f"Raza: {animal.raza}")