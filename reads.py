import data
import datetime as dt

#Nueva chamba
#Este es una prueba
bd = data.datos
times = data.times

def search(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("Encontrado")
            return True
        else:
            return False
        



def val_dnitype(dni):
    #Es 0 si no está en la base de datos
    #Es 1 si está en la base de datos
    if len(str(dni)) == 8:
        return search(dni)
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
        return[access, gate]
    else:
        print("Usted no tiene acceso")
        return[0,0]
    
def reservation_now():
    ava_g = available_gate()
    #Si no hay puerta disponible
    if ava_g == 0:
        print("No hay puerta disponible")
        return 0
    else:
        return [ava_g,1]
    

def day_():
    x= dt.date.today()
    x_str = f'{x.day}/{x.month}/{x.year}'
    return x_str
def time_():
    hour_ = dt.datetime.now()
    if int(hour_.hour)>12:
        str_hour =f'{hour_.hour-12}:00pm'
    elif int(hour_.hour)<12:
        str_hour =f'{hour_.hour}:00am'
    else:
        str_hour =f'{hour_.hour}:00m'
    return str_hour

    return None


def val_gate(day, time):
    for entry in times:
        if entry['day'] == day:
            for time_entry in entry['times']:
                if time_entry['time'] == time:
                    for gate_entry in time_entry['gates']:
                        if gate_entry['reserva'] == '0':
                            print(f"La puerta {gate_entry['gate']} está disponible.")
                            return gate_entry
                        else:
                            print("No hay puertas disponibles en este momento.")
                    return 0
                else:
                    print("La hora especificada no está disponible para reservas.")
            return 0
        else:
            print("El día especificado no está en la base de datos.")
    return 0



    
def available_gate():
    _day = day_()
    _time = time_()
    
    return val_gate(_day,_time)




