#Gate 0 es no reserva

datos = [{
    'DNI': '70398195', 
    'USUARIO':'Sofia Bobadilla', 
    'Reserva': 1, 'Puerta' : 1
},
{
    'DNI': '78371283', 
    'USUARIO':'Carlos Oliva', 
    'Reserva': 0, 'Puerta' : 0
},
{
    'DNI': '12345678', 
    'USUARIO':'Fabrizio Piedra', 
    'Reserva': 1, 'Puerta' : 2
},
]


times =[
    { 'day':'10/11/2023', 
     'times':[{'time':'8:00pm','gates':[{'gate':1,'reserva':'0'},{'gate':2,'reserva':'0'}]},
              {'time':'9:00pm','gates':[{'gate':1,'reserva':'0'},{'gate':2,'reserva':'0'}]}]   
    },

    { 'day':'11/11/2023', 
     'times':[{'time':'8:00pm','gates':[{'gate':1,'reserva':'1'},{'gate':2,'reserva':'0'}]},
              {'time':'9:00pm','gates':[{'gate':1,'reserva':'0'},{'gate':2,'reserva':'0'}]}]    
    },
]