class Cuenta:
    def __init__(self, nro_cuenta, nombre, monto):
        self.nro_cuenta = nro_cuenta
        self.nombre = nombre
        self.monto = monto
    def depositar(self, monto):
        if monto <= 0:
            print("Ingresa un numero positivo")
            return
        self.monto += monto
        print(f"Deposito realizado,saldo: {self.monto} ")
    def retirar(self, monto):
        if monto <= 0:
            print("Ingresa un numero positivo")
            return
        if monto >= self.monto:
            print("Saldo insuficiente")
            return
        self.monto -= monto
        print(f"Retiro realizado,saldo: {self.monto} ")

cuentas = []

def registrar():
    nombre = input("Ingresa el nombre:\n")
    nro_cuenta = int(input("Ingresa el numero de cuenta:\n"))
    monto = int(input("Ingresa el monto inicial:\n"))
    nueva_cuenta = Cuenta(nro_cuenta,nombre, monto)
    cuentas.append(nueva_cuenta)
    print("Cuenta registrada con éxito")


def listarCuentas():
    for c in cuentas:
        print("=======================")
        print(f"Nombre: {c.nombre}")
        print(f"Nro. Cuenta: {c.nro_cuenta}")
        print(f"Saldo: {c.monto}")
        print("=======================")

def buscarCuenta(nro_cuenta):
    for c in cuentas:
        if c.nro_cuenta == nro_cuenta:
            print("Cuenta encontrada!")
            return c
    print("cuenta no encontrada")
    return False

def realizarDeposito():
    nro_cuenta = int(input("Ingresa el numero de la cuenta\n"))
    cuenta = buscarCuenta(nro_cuenta)
    if cuenta:
        monto = int(input("ingresa el monto a depositar\n"))
        cuenta.depositar(monto)

def realizarRetiro():
    nro_cuenta = int(input("Ingresa el numero de la cuenta\n"))
    cuenta = buscarCuenta(nro_cuenta)
    if cuenta:
        monto = int(input("ingresa el monto a retirar\n"))
        cuenta.retirar(monto)
def menu():

    resp = True
    while resp:
        print("===================================")
        print("Menu interactivo")
        print("1. Registrar cuenta")
        print("2. Listar cuentas")
        print("3. Realizar Deposito")
        print("4. Realizar retiro")
        print("5. Salir")
        print("===================================")
        entrada = input("ingresa una opcion:\n")
        print("===================================")
        
        match entrada:
            case "1":
                registrar()
            case "2":
                listarCuentas()
            case "3":
                realizarDeposito()
            case "4":
                realizarRetiro()
            case _:
                resp = False
menu()