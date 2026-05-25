import time
import cProfile
import pstats
import io
import math
import numpy as np

# codigo optimizado
# aplica 3 mejoras: iterar solo hasta la raiz cuadrada, criba con numpy
# y una list comprehension para armar la lista final


def buscarPrimosOptimizado(limiteRango):
    # array booleano de numpy, al inicio todos se asumen primos
    sonPrimos = np.ones(limiteRango + 1, dtype=bool)
    sonPrimos[0] = False
    sonPrimos[1] = False

    # mejora 1: solo necesitamos llegar hasta la raiz cuadrada del limite
    limiteRaiz = int(math.sqrt(limiteRango)) + 1

    for numeroActual in range(2, limiteRaiz):
        if sonPrimos[numeroActual]:
            # mejora 3: numpy marca todos los multiplos de golpe sin bucle interno
            sonPrimos[numeroActual * numeroActual::numeroActual] = False

    # mejora 2: list comprehension para construir la lista de primos
    listaPrimos = [numero for numero in np.where(sonPrimos)[0]]
    return listaPrimos


limiteBusqueda = 100000

print("buscando primos del 1 al 100000 CON optimizacion")

tiempoInicio = time.time()
listaResultado = buscarPrimosOptimizado(limiteBusqueda)
tiempoFin = time.time()

tiempoTotal = tiempoFin - tiempoInicio

print(f"cantidad de primos encontrados: {len(listaResultado)}")
print(f"tiempo de ejecucion: {tiempoTotal:.6f} segundos")

archivoTiempo = open("tiempo_optimizado.txt", "w")
archivoTiempo.write(str(tiempoTotal))
archivoTiempo.close()
print("tiempo guardado en tiempo_optimizado.txt")

# profiling con cProfile xq la tarea pide detectar las funciones criticas
print("generando profiling del codigo optimizado")
perfilador = cProfile.Profile()
perfilador.enable()
buscarPrimosOptimizado(limiteBusqueda)
perfilador.disable()

bufferSalida = io.StringIO()
estadisticas = pstats.Stats(perfilador, stream=bufferSalida)
estadisticas.sort_stats("cumulative")
estadisticas.print_stats()

archivoProfiling = open("profiling_optimizado.txt", "w")
archivoProfiling.write(bufferSalida.getvalue())
archivoProfiling.close()
print("profiling guardado en profiling_optimizado.txt")
