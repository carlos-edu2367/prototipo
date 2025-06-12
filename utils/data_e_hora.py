from datetime import datetime

def data_atual():
    data_e_hora = datetime.now()
    data = data_e_hora.date()

    return data

def hora_atual():
    data_e_hora = datetime.now()
    hora = data_e_hora.time()

    return hora