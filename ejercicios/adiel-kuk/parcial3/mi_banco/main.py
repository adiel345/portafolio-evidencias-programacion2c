from banco import Banco
from cuenta import Cuenta

def main():from banco import Banco
from cuenta import Cuenta

class SistemaBanco:

    def _init_(self):
        self.banco = Banco()

    def menu(self):

        while True:

            print("\n========== BANCO ==========")
            print("1. Crear cuenta")
            print("2. Mostrar clientes")
            print("3. Depositar dinero")
            print("4. Retirar dinero")
            print("5. Transferir dinero")
            print("6. Buscar cuenta")
            print("7. Eliminar cuenta")
            print("8. Salir")

            opcion = input("Selecciona una opción: ")

            # Crear cuenta
            if opcion == "1":

                nombre = input("Nombre del cliente: ")
                numero = input("Número de cuenta: ")

                try:
                    saldo = float(input("Saldo inicial: "))
                except ValueError:
                    saldo = 0

                nueva = Cuenta(nombre, numero, saldo)

                self.banco.registrar_cuenta(nueva)

                print("Cuenta registrada correctamente.")

            # Mostrar clientes
            elif opcion == "2":

                if len(self.banco.cuentas) == 0:

                    print("No hay cuentas registradas.")

                else:

                    for c in self.banco.cuentas:

                        print("\nCliente:", c.cliente)
                        print("Cuenta:", c.num_cuenta)
                        print("Saldo:", c.saldo)

            # Depositar
            elif opcion == "3":
                print("Función depósito en proceso.")
            # Retirar
            elif opcion == "4":
                print("Función retiro en proceso.")
            # Transferir
            elif opcion == "5":
                print("Función transferencia en proceso.")
            # Buscar
            elif opcion == "6":
                print("Función búsqueda en proceso.")
            # Eliminar
            elif opcion == "7":
                print("Función eliminar en proceso.")
            # Salir
            elif opcion == "8":
                print("Programa finalizado.")
                break
            else:
                print("Opción incorrecta.")


if __name__ == "_main_":

    app = SistemaBanco()
    app.menu()


    if __name__ == "__main__":
    
       main()