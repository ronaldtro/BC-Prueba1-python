import time 

def listaFechaHora():
    tiempoSegundos = time.time()
    tiempoFormateado = time.ctime(tiempoSegundos)
    tiempoLista = tiempoFormateado.split()
    
    return tiempoLista