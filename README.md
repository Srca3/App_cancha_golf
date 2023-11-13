# Grupo 6
## Integrantes
Cruz Alayza, Santiago Ricardo \
Doig Cochrane, Lucas \
Ibáñez Calderón, Luis Carlo\
Morocho Cruz, Zebastian\
Oliva Mendoza, Carlos Ernesto\
Piedra Valencia, Fabrizio Aaron\
Vásquez Martínez, Diego Martín

# App_cancha_golf

Este es un sistema simple de control de acceso que permite a los usuarios acceder a una cancha de golf o reservar una cancha en función de su DNI y disponibilidad. El sistema incluye funciones para verificar el DNI, buscar en la base de datos, reservar puertas y más.

## Requisitos

Asegúrate de tener instalado Python en tu sistema para ejecutar este código.

## Uso

1. Clona el repositorio en la carpeta que desees.
    ```bash
    git clone https://github.com/Srca3/App_cancha_golf.git
    ```
2. Configura las conexiones serie(USB) entre la Raspberry Pi y el Arduino. Así como las conexiones físicas del arduino.
3. Asegurate que la base de datos(diccionarios) en el archivo `data.py` este actualizada.
3. Asegurate de tener instalados los paquetes necesarios.
    ```python
    pip install datetime serial time pyserial
    ```
4. Abre la terminal en la ubicación del archivo `main.py`.
5. Ejecuta el script usando `python main.py`.
   ```bash
    python main.py
    ```
6. Sigue las instrucciones proporcionadas para ingresar tu DNI y realizar reservas.

## Funciones Principales

### `access()`

Permite a los usuarios ingresar su DNI y verifica si tienen acceso. Si no, ofrece la opción de reservar una puerta.

### `val_dnitype(dni)`

Verifica la validez del DNI y busca si está en la base de datos.

### `send_to_arduino(puerta)`

Envia de modo serial el codigo a Arduino y recibe una respuesta, confirmando si la conexión se realizo de manera satisfactoria o no.

### `dni_reads(dni)`

Lee el DNI, verifica el acceso y la puerta asignada.

### `reservation_now()`

Permite realizar una reserva inmediata si hay puertas y horarios disponibles.

### `available_gate()`

Verifica la disponibilidad de puertas en función de la fecha y hora actuales.

## Estructura del Proyecto

- `main.py`: Contiene el código principal.
- `assets.py`: Contiene la funcíon principal access() y funciones adicionales como save() y send_to_arduino().
- `data.py`: Contiene datos de ejemplo y funciones relacionadas con la base de datos.
- `reads.py`: Contiene funciones relacionadas con la lectura y verificación del DNI.
- `opendoor.ino`: Este archivo es el codigo que será subido al arduino.

## Contribuir

Si encuentras algún problema o deseas contribuir, ¡sientete libre de abrir un issue o enviar un pull request!


