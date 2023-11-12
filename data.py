#Gate 0 es no reserva

datos = [
{   'DNI': '70398195', 
    'USUARIO':'Sofia Bobadilla', 
    'Reserva': 1,
    'Puerta' : 1,
},
{   'DNI': '78371283', 
    'USUARIO':'Carlos Oliva', 
    'Reserva': 0, 
    'Puerta' : 0,
},
{   'DNI': '72633889', 
    'USUARIO':'Santiago Cruz', 
    'Reserva': 1, 
    'Puerta' : 2,
}
]

times = [
    {'day': '10/11/2023',
     'times': [
         {'time': '8:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '9:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '10:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '11:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '12:00m', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '1:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '2:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '3:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '4:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '5:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '6:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '7:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '8:00pm', 'gates': [{'gate': 1, 'reserva': '1'}, {'gate': 2, 'reserva': '1'}]},
         {'time': '9:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]}
     ]
    },

    {'day': '11/11/2023',
     'times': [
         {'time': '8:00am', 'gates': [{'gate': 1, 'reserva': '1'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '9:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '10:00am', 'gates': [{'gate': 1, 'reserva': '1'}, {'gate': 2, 'reserva': '1'}]},
         {'time': '11:00am', 'gates': [{'gate': 1, 'reserva': '1'}, {'gate': 2, 'reserva': '1'}]},
         {'time': '12:00m', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '1:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '2:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '3:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '4:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '5:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '6:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '7:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '8:00pm', 'gates': [{'gate': 1, 'reserva': '1'}, {'gate': 2, 'reserva': '1'}]},
         {'time': '9:00pm', 'gates': [{'gate': 1, 'reserva': '1'}, {'gate': 2, 'reserva': '1'}]}
     ]
    },

    {'day': '12/11/2023',
     'times': [
         {'time': '8:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '9:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '10:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '11:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '12:00m', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '1:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '2:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '3:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '4:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '5:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '6:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '7:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '8:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '9:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]}
     ]
    },

    {'day': '13/11/2023',
     'times': [
         {'time': '8:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '9:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '10:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '11:00am', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '12:00m', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '1:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '2:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '3:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '4:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '5:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '6:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '7:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '8:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]},
         {'time': '9:00pm', 'gates': [{'gate': 1, 'reserva': '0'}, {'gate': 2, 'reserva': '0'}]}
     ]
    },
]
