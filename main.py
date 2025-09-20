from pathlib import Path
import sys
import time

class RegistroUsuario:
    def __init__(self, nombre="", contrasena=""):
        self.nombre = nombre
        self.contrasena = contrasena
        self.base = Path("usuarios-y-contrasenas")
        self.base.mkdir(exist_ok=True)

    def crear_usuario(self):
        print('----------------------------------')
        print('           REGISTRARSE')
        print('')
        self.nombre = input('Ingresa tu nombre de usuario: ')
        self.contrasena = input('Ingresa una contraseña segura: ')
        print('')
        print('----------------------------------')

        carpeta = self.base / self.nombre
        carpeta.mkdir(exist_ok=True)

        with open(carpeta / "datos.txt", "w", encoding="utf-8") as f:
            f.write(self.contrasena + "\n0")
        time.sleep(2)
        print("Usuario registrado con éxito.")

    def iniciar_sesion(self):
        while True:
            print('-----------------------------------')
            print('         INICIAR SESIÓN')
            print('')
            nombre = input('Ingresa tu nombre: ')
            if nombre.lower() == 'salir':
                print('¡Hasta la próxima!')
                sys.exit()

            contrasena = input('Ingresa tu contraseña: ')
            if contrasena.lower() == 'salir':
                print('¡Hasta la próxima!')
                sys.exit()

            carpeta = self.base / nombre / "datos.txt"
            if carpeta.exists():
                with open(carpeta, "r", encoding="utf-8") as f:
                    guardada, saldo = f.read().splitlines()

                if guardada == contrasena:
                    print("Usuario logeado con éxito!")
                    self.nombre = nombre
                    self.contrasena = contrasena
                    return int(saldo)
                else:
                    print("Contraseña incorrecta. Inténtalo de nuevo.")
            else:
                print("El usuario no existe. Inténtalo de nuevo.")


class Banco(RegistroUsuario):
    def __init__(self, nombre="", contrasena="", saldo=0):
        super().__init__(nombre, contrasena)
        self.saldo = saldo

    def guardar_datos(self):
        carpeta = self.base / self.nombre / "datos.txt"
        with open(carpeta, "w", encoding="utf-8") as f:
            f.write(self.contrasena + "\n" + str(self.saldo))

    def elegir_accion(self):
        while True:
            time.sleep(5)
            print('-------------------------------------------')
            print('            ELIJE UNA OPCIÓN')
            print('')
            print('    1. Ingresar dinero')
            print('    2. Retirar dinero')
            print('    3. Mostrar información de la cuenta')
            print('    4. Salir del programa')
            print('-------------------------------------------')
            eleccion = input('> ')

            if eleccion == '1':
                self.meter_dinero()
            elif eleccion == '2':
                self.sacar_dinero()
            elif eleccion == '3':
                self.mostrar_informacion()
            elif eleccion == '4':
                print('¡Hasta la próxima!')
                self.guardar_datos()
                sys.exit()
            else:
                print("Opción no válida.")

    def meter_dinero(self):
        cantidad = int(input("¿Cuánto quieres ingresar? "))
        self.saldo += cantidad
        print(f"Has ingresado {cantidad}€. Saldo actual: {self.saldo}€")
        self.guardar_datos()

    def sacar_dinero(self):
        cantidad = int(input("¿Cuánto quieres retirar? "))
        if cantidad > self.saldo:
            print("No tienes suficiente saldo.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad}€. Saldo actual: {self.saldo}€")
        self.guardar_datos()

    def mostrar_informacion(self):
        print(f"Usuario: {self.nombre}")
        print(f"Saldo: {self.saldo}€")

        
        
        
        
usuarios = RegistroUsuario()
preguntar = input('¿Qué quieres hacer?\n1. Registrarse\n2. Iniciar sesión\n\n> ')

if preguntar.lower() in ['registrarse', '1']:
    usuarios.crear_usuario()
    banco = Banco(usuarios.nombre, usuarios.contrasena, 0)
    banco.elegir_accion()

elif preguntar.lower() in ['iniciar sesion', '2']:
    saldo_inicial = usuarios.iniciar_sesion()
    banco = Banco(usuarios.nombre, usuarios.contrasena, saldo_inicial)
    banco.elegir_accion()





        

