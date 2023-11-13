#Grupo 6 
#Integrantes:
#Cruz Alayza, Santiago Ricardo 
#Doig Cochrane, Lucas 
#Ibáñez Calderón, Luis Carlo 
#Morocho Cruz, Zebastian 
#Oliva Mendoza, Carlos Ernesto 
#Piedra Valencia, Fabrizio Aaron 
#Vásquez Martínez, Diego Martín 

 
import assets
def main(): 
    while True:
        results = assets.access()
        assets.save()
        assets.send_to_arduino(results[1])
if __name__ =='__main__':
        main()