## Bitbill - Generador de Monedas Ficticias

### Descripción
Bitbill es un programa que permite generar monedas ficticias de diferentes tipos y realizar operaciones básicas con ellas, como visualizar el wallet digital, extraer fondos a través de PayPal y minar una moneda especial llamada bitbill.

### Paquetes necesarios
El programa requiere los siguientes paquetes de Python:

- `random`: Para generar valores aleatorios.
- `uuid`: Para generar identificadores únicos para las monedas.
- `argparse`: Para manejar argumentos de línea de comandos (no utilizado en esta versión).
- `os`: Para limpiar la pantalla.
- `datetime`: Para manejar fechas y tiempos.
- `paypalrestsdk`: Para realizar extracciones de fondos a través de PayPal (no implementado en esta versión).

### Instrucciones de uso
1. Clona el repositorio o descarga los archivos de Bitbill.
2. Asegúrate de tener instalado Python en tu sistema.
3. Instala los paquetes necesarios mencionados anteriormente mediante pip:
   ```
   pip install paypalrestsdk
   ```
4. Abre una terminal o línea de comandos y navega hasta la ubicación del archivo `bitbill.py`.
5. Ejecuta el programa utilizando el siguiente comando:
   ```
   python bitbill.py
   ```
6. Sigue las instrucciones en pantalla para interactuar con el programa.
7. Elige la opción "login" para iniciar sesión y acceder al wallet digital.
8. Utiliza las opciones disponibles para ver el wallet, extraer fondos o minar bitbill.

### Características principales
- Generación de monedas ficticias: El programa genera monedas ficticias de diferentes tipos (Bitcoin, Ethereum, Litecoin, Ripple, Monero) con identificadores únicos y valores aleatorios.
- Visualización del wallet digital: Permite ver el wallet digital que contiene las monedas generadas, mostrando el tipo de moneda y su valor en euros.
- Extracción de fondos: Ofrece la posibilidad de extraer fondos del wallet utilizando el método de pago PayPal. El usuario debe proporcionar su correo de PayPal y la cantidad a extraer.
- Minería de bitbill: Permite minar la moneda especial llamada bitbill, que tiene un valor específico. La cantidad minada depende del día en que se realice la acción, aumentando en 1 cada dos días.

¡Disfruta de Bitbill y explora las diversas funcionalidades que ofrece!
