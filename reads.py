import data

bd = data.datos

def search(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("Encontrado")
            return True
        else:
            return False
        

def caca(dni):
    x=input("ingrese algo")
    print(x)
    return  x
    



def val_dnitype(dni):
    #Es 0 si no está en la base de datos
    #Es 1 si está en la base de datos
    if len(str(dni)) == 8:
        search(dni)
    else: 
        raise Exception("DNI inválido")
        return False
    

def reserved_gate(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            gate = (dato['Puerta'])
    return gate


def have_permission(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            access = (dato['Reserva'])
    return access


def dni_reads(dni):
    print("Leyendo DNI")
    val_access = val_dnitype(dni) # Puede ser 0 o 1 
    if val_access == True:
        gate = reserved_gate(dni) #Puerta o cancha
        access = have_permission(dni) # Tiene acceso o no
        return[gate, access]
    else:
        print("Usted no tiene acceso")
        return[0,0]
    
def reservation_now():
    print("reserva ahora")



