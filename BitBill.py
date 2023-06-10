import random
import uuid
import argparse
import os
import datetime
import paypalrestsdk

class MonedaFicticia:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

def generar_monedas(cantidad):
    monedas = []
    for _ in range(cantidad):
        # Generar una moneda ficticia aleatoria
        moneda = random.choice(["Bitcoin", "Ethereum", "Litecoin", "Ripple", "Monero"])

        # Generar un identificador único para la moneda
        identificador = str(uuid.uuid4())

        # Asignar un valor aleatorio a la moneda
        valor = round(random.uniform(0.01, 1000), 2)

        # Crear una instancia de la clase MonedaFicticia
        moneda_obj = MonedaFicticia(moneda, valor)

        # Almacenar la moneda en la lista de monedas generadas
        monedas.append((identificador, moneda_obj))

    return monedas

def mostrar_monedas(monedas):
    print("Monedas generadas:")
    for identificador, moneda in monedas:
        print(f"ID: {identificador}, Moneda: {moneda.nombre}, Valor: {moneda.valor}")

def minar_bitbill(dia):
    cantidad_bitbill = 1
    if dia == 1:
        cantidad_bitbill = 10
    elif dia % 2 == 0:
        cantidad_bitbill += (dia // 2)

    valor_bitbill = 20 * cantidad_bitbill

    print(f"¡Has minado {cantidad_bitbill} bitbill! El valor total es de {valor_bitbill}€.")

    # Agregar las monedas minadas al wallet
    moneda_obj = MonedaFicticia("bitbill", valor_bitbill)
    monedas_generadas.append((str(uuid.uuid4()), moneda_obj))

def iniciar_sesion():
    wallet = input("Ingrese el nombre de su billetera digital: ")
    print(f"Bienvenido/a, {wallet}!")

    client_id = input("Ingrese su Client ID de PayPal: ")
    client_secret = input("Ingrese su Client Secret de PayPal: ")

    dia_actual = datetime.datetime.now().day

    while True:
        opcion_menu = input("Ingrese 'bit wallet' para ver el wallet digital, 'extraer' para extraer el wallet, 'minar' para minar bitbill o 'salir' para finalizar: ")

        if opcion_menu == "bit wallet":
            wallet_info = {}
            for identificador, moneda in monedas_generadas:
                if moneda.nombre not in wallet_info:
                    wallet_info[moneda.nombre] = moneda.valor
                else:
                    wallet_info[moneda.nombre] += moneda.valor

            print("Wallet digital:")
            for moneda, valor in wallet_info.items():
                print(f"Moneda: {moneda}, Valor: {valor * 20}€")

        elif opcion_menu == "extraer":
            metodo_pago = input("Ingrese el método de pago para extraer el wallet (PayPal, tarjeta de crédito, etc.): ")
            if metodo_pago.lower() == "paypal":
                correo_paypal = input("Ingrese su correo de PayPal: ")
                cantidad_paypal = float(input("Ingrese la cantidad a extraer a PayPal: "))
                if cantidad_paypal > sum(moneda.valor for _, moneda in monedas_generadas):
                    print("Error: No tiene suficiente saldo en su wallet.")
                else:
                    # Procesar la extracción a PayPal
                    realizar_extraccion_paypal(client_id, client_secret, correo_paypal, cantidad_paypal)

            else:
                print("Método de pago no válido. Intente nuevamente.")

        elif opcion_menu == "minar":
            minar_bitbill(dia_actual)

        elif opcion_menu == "salir":
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def mostrar_ayuda():
    print("""
Comandos disponibles:
    bit wallet: Ver el wallet digital de las monedas generadas.
    bit -help: Mostrar la ayuda del programa.
    """)

# Menú principal
def menu_principal():
    print("********************")
    print("Bienvenido al generador de monedas")
    print("********************")
    print()
    while True:
        opcion_menu = input("Ingrese 'login' para iniciar sesión o 'salir' para finalizar: ")
        if opcion_menu == "login":
            iniciar_sesion()
        elif opcion_menu == "salir":
            break
        elif opcion_menu == "bit -help":
            mostrar_ayuda()
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Limpia la pantalla según el sistema operativo
def limpiar_pantalla():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    limpiar_pantalla()

    # Verificar el plazo de 24 horas
    ultima_ejecucion = datetime.datetime.now()
    if os.path.exists("ultima_ejecucion.txt"):
        with open("ultima_ejecucion.txt", "r") as file:
            ultima_ejecucion = datetime.datetime.strptime(file.read(), "%Y-%m-%d %H:%M:%S")

    tiempo_transcurrido = datetime.datetime.now() - ultima_ejecucion
    if tiempo_transcurrido.total_seconds() < 86400:  # 24 horas en segundos
        print("No puedes utilizar el programa hasta que haya transcurrido un plazo de 24 horas desde la última vez que lo ejecutaste.")
        exit()

    # Generar monedas ficticias
    cantidad_monedas = int(input("Ingrese la cantidad de monedas a generar: "))
    monedas_generadas = generar_monedas(cantidad_monedas)

    # Mostrar monedas generadas
    mostrar_monedas(monedas_generadas)

    # Ejecutar el menú principal
    menu_principal()

    # Guardar la fecha y hora de la última ejecución
    with open("ultima_ejecucion.txt", "w") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
