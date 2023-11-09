import reads
num_gate = 2 
in_gate = 0 # Inicialmente la puerta esta cerrada

def access():
    dni = input('Ingrese DNI: ') #Esto puede cambiarse por un sensor
    reserve = reads.dni_reads(dni)
    if reserve == False:
        reads.reservation_now()
    else:
        access_val = reserve[0]
        gate = reserve[1]

    return [access_val,gate] #La puerta tiene que abrirse o cerrarse
def save():
    return None
def send():
    return None
