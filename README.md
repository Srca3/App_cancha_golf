# Grupo 6
## Autores
Santiago Cruz 
Carlos Oliva
Diego Vasquez
Luis Ibañez
Lucas Doig
Fabrizio Piedra
Zebastian Morocho

# App_cancha_golf

Este es un sistema simple de control de acceso que permite a los usuarios acceder a una cancha de golf o reservar una cancha en función de su DNI y disponibilidad. El sistema incluye funciones para verificar el DNI, buscar en la base de datos, reservar puertas y más.

## Requisitos

Asegúrate de tener instalado Python en tu sistema para ejecutar este código.

## Uso

1. Clona el repositorio en la carpeta que desees.
    ```bash
    git clone https://github.com/Srca3/App_cancha_golf
    ```
2. Asegurate de tener instalados los paquetes necesarios.
    ```python
    pip install datetime serial time pyserial
    ```
3. Abre la terminal en la ubicación del archivo `main.py`.
4. Ejecuta el script usando `python main.py`.
5. Sigue las instrucciones proporcionadas para ingresar tu DNI y realizar reservas.

## Funciones Principales

### `access()`

Permite a los usuarios ingresar su DNI y verifica si tienen acceso. Si no, ofrece la opción de reservar una puerta.

### `val_dnitype(dni)`

Verifica la validez del DNI y busca si está en la base de datos.

### `dni_reads(dni)`

Lee el DNI, verifica el acceso y la puerta asignada.

### `reservation_now()`

Permite realizar una reserva inmediata si hay puertas disponibles.

### `available_gate()`

Verifica la disponibilidad de puertas en función de la fecha y hora actuales.

## Estructura del Proyecto

- `main.py`: Contiene el código principal.
- `assets.py`: Contiene la funcíon principal access() y funciones adicionales como save() y send().
- `data.py`: Contiene datos de ejemplo y funciones relacionadas con la base de datos.
- `reads.py`: Contiene funciones relacionadas con la lectura y verificación del DNI.

## Contribuir

Si encuentras algún problema o deseas contribuir, ¡sientete libre de abrir un issue o enviar un pull request!


