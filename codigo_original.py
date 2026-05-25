import time

# codigo original sin optimizar
# busca los numeros primos del 1 al 100000 revisando todos los divisores
# es lento a proposito xq sirve como punto de comparacion


def buscarPrimosSinOptimizar(limiteRango):
    listaPrimos = []
    # recorremos cada numero del 2 hasta el limite
    for numeroActual in range(2, limiteRango + 1):
        esPrimo = True
        # aqui esta el problema: revisamos TODOS los divisores hasta el numero
        for divisor in range(2, numeroActual):
            if numeroActual % divisor == 0:
                esPrimo = False
                break
        if esPrimo:
            listaPrimos.append(numeroActual)
    return listaPrimos


limiteBusqueda = 100000

print("buscando primos del 1 al 100000 sin optimizacion")
print("esto puede tardar un poco, espere por favor")

tiempoInicio = time.time()
listaResultado = buscarPrimosSinOptimizar(limiteBusqueda)
tiempoFin = time.time()

tiempoTotal = tiempoFin - tiempoInicio

print(f"cantidad de primos encontrados: {len(listaResultado)}")
print(f"tiempo de ejecucion: {tiempoTotal:.4f} segundos")

# guardamos el tiempo para usarlo despues en los graficos
archivoTiempo = open("tiempo_original.txt", "w")
archivoTiempo.write(str(tiempoTotal))
archivoTiempo.close()
print("tiempo guardado en tiempo_original.txt")
