class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = []

def registrar():
    nombre = input("Ingresa el nombre:")
    edad = int(input("Ingresa la edad:\n"))
    nueva_persona = Persona(nombre, edad)
    personas.append(nueva_persona)
    print("Peronsa registrada con éxito")


def listarPersonas():
    for p in personas:
        print("=======================")
        print(f"Nombre: {p.nombre}")
        print(f"Edad: {p.edad}")
        print("=======================")
def menu():

    resp = True
    while resp:
        print("===================================")
        print("Menu interactivo")
        print("1. Registrar persona")
        print("2. Listar Personas")
        print("3. Salir")
        print("===================================")
        entrada = input("ingresa una opcion:\n")
        print("===================================")
        
        match entrada:
            case "1":
                registrar()
            case "2":
                listarPersonas()
            case _:
                resp = False
menu()