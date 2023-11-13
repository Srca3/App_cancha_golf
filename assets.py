import reads
import serial
import time
in_gate = 0 # Inicialmente la puerta esta cerrada

def access():
    reads._now()
    dni = input('Ingrese DNI: ') #Esto puede cambiarse por un sensor
    reserve = reads.dni_reads(dni)
    if reserve == [0,0] and reads.search(dni)==False :
        print("El dni no esta en la base de datos")
        print('Ingrese un nuevo DNI.')
        return access()
    elif reserve ==[0,0] and reads.search(dni)==True:
        _action = input("Ingresa s o n para definir si quieres reservar ahora: ")
        if _action =='s':
            reservation_result=reads.reservation_now()
            access_val = reservation_result[0]
            gate = reservation_result[1]        
            if gate ==0:
                print(f"Lo lamentamos {reads.user(dni)}, no hay cancha disponible.")
                print("No se abrira ninguna puerta.")
                return[access_val,gate]
            print(f"Bienvenido {reads.user(dni)}, la cancha {gate} está disponible.")
            return [access_val,gate]
        else:
            print("Solicitó no reservar ahora.")
            return access()
    else:
        access_val = reserve[0]
        gate = reserve[1]
        print("Bienvenido {}. Tu cancha reservada es la {}.".format(reads.user(dni),gate))
        return [access_val,gate] #La puerta tiene que abrirse o cerrarse

def save():
    print("Guardando...")
    return None


def send_to_arduino(puerta):
    print(f'El valor que se enviara al raspberry será: {puerta}')
    try:
        # Configura la conexión serial con el Arduino
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Ajusta el puerto serial según sea necesario
        time.sleep(2)  # Espera 2 segundos para establecer la conexión

        # Envía el valor de la puerta al Arduino
        ser.write(f"{puerta}\n".encode('utf-8'))

        # Espera la confirmación del Arduino (opcional)
        response = ser.readline().decode('utf-8').strip()
        print(f"Arduino dice: {response}.")

        # Cierra la conexión serial
        ser.close()

    except Exception as e:
        print(f"Error al enviar datos al Arduino: {e}")

