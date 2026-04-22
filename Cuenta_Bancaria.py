#Cambio final
from os import system
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_clinete(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: ${self.balance}"

    def depositar(self):
        deposito = float(input("Monto del a depositar: "))
        self.balance += deposito
        return self.balance

    def retirar(self):
        retiro = float(input("Monto a retirar: "))
        while retiro > self.balance:
            print(f"El monto que desea retirar es superior al saldo disponible.\nSaldo disponible: {self.balance}")
            retiro = float(input("Monto a retirar: "))
        else:
            self.balance -= retiro
            return self.balance

#Funciones
def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el numero de cuenta del cliente: ")
    balance = float(input("Ingrese el saldo del cliente: "))
    limpiar_consola()

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente


def eleccion_usuario():
    titulo = "Menu de opciones".center(30,"*").upper()
    print(
        titulo + """
            [1] Depositar
            [2] Retirar
            [3] Salir""")
    seleccion = int(input("Seleccione la opción que desea realizar: "))
    while seleccion not in [1,2,3]:
        print("Opción incorrecta")
        seleccion = int(input("Seleccione la opción que desea realizar: "))
    else:
        return seleccion


def limpiar_consola():
    system("clear")


def inicio():
    try:#Evita pantalla de error al cortar la ejecución del program con stop
        cliente = crear_cliente()
        seleccion = eleccion_usuario()
        while seleccion != 3:
            match seleccion:
                case 1:
                    cliente.depositar()
                    limpiar_consola()
                    print(cliente.imprimir_clinete()+"\n")
                    seleccion = eleccion_usuario()
                case 2:
                    cliente.retirar()
                    limpiar_consola()
                    print(cliente.imprimir_clinete()+"\n")
                    seleccion = eleccion_usuario()
        else:
            limpiar_consola()
            print("Fin del programa")
    except KeyboardInterrupt:#Mensaje cuando se corta la ejecución forzosamente
        print("\n\nPrograma finalizado por el usuario. ¡Hasta pronto!")

inicio()