
def imprimir():
    print("imprimiendo algo")

def saludo():
    person = input("Ingresa tu nombre\n")
    print(f"Hola {person}")
def menu():

    resp = True
    while resp:
        print("===================================")
        print("Menu interactivo")
        print("1. Imprimir")
        print("2. Saludar")
        print("3. Salir")
        print("===================================")
        entrada = input("ingresa una opcion:\n")
        print("===================================")
        
        match entrada:
            case "1":
                imprimir()
            case "2":
                saludo()
            case _:
                resp = False
menu()