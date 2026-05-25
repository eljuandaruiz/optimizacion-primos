import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# script q lee los tiempos guardados y arma los 2 graficos q pide la tarea
# uno de barras comparando y otro de torta con la distribucion


def leerTiempoDeArchivo(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    valor = float(archivo.read().strip())
    archivo.close()
    return valor


tiempoOriginal = leerTiempoDeArchivo("tiempo_original.txt")
tiempoOptimizado = leerTiempoDeArchivo("tiempo_optimizado.txt")

# grafico 1: comparativa de tiempos con barras
figuraBarras, ejeBarras = plt.subplots(figsize=(6, 4.5))
versiones = ["Original", "Optimizado"]
tiempos = [tiempoOriginal, tiempoOptimizado]
barras = ejeBarras.bar(versiones, tiempos, color=["#d9534f", "#5cb85c"])
ejeBarras.set_ylabel("Tiempo (segundos)")
ejeBarras.set_title("Comparativa de tiempos: original vs optimizado")
for barra, valor in zip(barras, tiempos):
    ejeBarras.text(barra.get_x() + barra.get_width() / 2, valor,
                   f"{valor:.4f}s", ha="center", va="bottom", fontsize=9)
figuraBarras.tight_layout()
figuraBarras.savefig("grafico_comparativa_tiempos.png", dpi=130)
plt.close(figuraBarras)

# grafico 2: distribucion del tiempo total en forma de torta
figuraTorta, ejeTorta = plt.subplots(figsize=(5.5, 5.5))
ejeTorta.pie(tiempos, labels=versiones, autopct="%1.2f%%",
             colors=["#d9534f", "#5cb85c"], startangle=90)
ejeTorta.set_title("Distribucion del tiempo total de ejecucion")
figuraTorta.tight_layout()
figuraTorta.savefig("grafico_distribucion_tiempos.png", dpi=130)
plt.close(figuraTorta)

print("graficos generados ok")
print(f"original: {tiempoOriginal:.4f}s   optimizado: {tiempoOptimizado:.6f}s")
factor = tiempoOriginal / tiempoOptimizado if tiempoOptimizado > 0 else 0
print(f"el optimizado es ~{factor:.0f}x mas rapido")
