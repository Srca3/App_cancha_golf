import reads
num_gate = 2 
in_gate = 0 # Inicialmente la puerta esta cerrada

def access():
    dni = input('Ingrese DNI: ') #Esto puede cambiarse por un sensor
    reserve = reads.dni_reads(dni)
    if reserve == [0,0] and reads.search(dni)==False :
        print("El dni no esta en la base de datos")
        print("Ingrese un nuevo DNI")
        access()
    elif reserve ==[0,0] and reads.search(dni)==True:
        _action = input("Ingresa s o n para definir si quieres reservar ahora")
        if _action =='s':
            reads.reservation_now()
        else:
            access()
    else:
        access_val = reserve[0]
        gate = reserve[1]
        print("La cancha es {}.".format(gate))
    return [access_val,gate] #La puerta tiene que abrirse o cerrarse
def save():
    return None
def send():
    return None
