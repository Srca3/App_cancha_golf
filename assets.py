import reads

in_gate = 0 # Inicialmente la puerta esta cerrada

def access():
    dni = input('Ingrese DNI: ') #Esto puede cambiarse por un sensor
    reserve = reads.dni_reads(dni)
    if reserve == [0,0] and reads.search(dni)==False :
        print("El dni no esta en la base de datos")
        print("Ingrese un nuevo DNI")
        access()
    elif reserve ==[0,0] and reads.search(dni)==True:
        _action = input("Ingresa s o n para definir si quieres reservar ahora: ")
        if _action =='s':
            access_val = reads.reservation_now()[0]
            gate = reads.reservation_now()[1]
            print(f"La puerta {gate} está disponible.")
            if gate ==0:
                print("No hay cancha disponible")
                print("No se abrira ninguna puerta")
                return[access_val,gate]
            return[access_val,gate]
        else:
            access()
    else:
        access_val = reserve[0]
        gate = reserve[1]
        usuario =reads.user(dni)
        print("Bienvenido {}. Tu cancha reservada es la {}.".format(usuario,gate))
        return [access_val,gate] #La puerta tiene que abrirse o cerrarse


def save():
    return None
def send_to_arduino(resultado):
    return None
