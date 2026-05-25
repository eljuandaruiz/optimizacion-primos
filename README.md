[DOCUMENTACION.md](https://github.com/user-attachments/files/28206346/DOCUMENTACION.md)
# DOCUMENTACION - Optimizacion de Codigo Python

**Materia:** Cultura Digital y Sociedad
**Estudiante:** Juan Ruiz
**Paralelo:** B

---

## 1. Introduccion

El codigo original busca los numeros primos del 1 al 100000. El problema q
tiene es q por cada numero revisa TODOS los divisores posibles desde 2 hasta
ese numero, lo cual genera muchisimas comparaciones innecesarias y lo hace
muy lento.

Problemas identificados:

- Bucle interno q llega hasta `n` en vez de hasta la raiz cuadrada de `n`
- No usa estructuras ni librerias optimizadas (numpy)
- Construye la lista con `.append()` dentro de un bucle

## 2. Optimizacion

Se aplicaron 3 tecnicas:

1. **Reduccion del rango del bucle:** se itera solo hasta `sqrt(n)` xq si un
   numero tiene un divisor mayor a su raiz, el divisor complementario ya
   aparecio antes
2. **List comprehension:** para armar la lista final de primos de forma mas
   eficiente q un bucle con append
3. **NumPy (Criba de Eratostenes):** un array booleano marca todos los
   multiplos de golpe con operaciones vectorizadas en vez de comparar uno x uno

## 3. Resultados

| Version | Tiempo de ejecucion | Primos encontrados |
|---|---|---|
| Original | 47.4026 s | 9592 |
| Optimizado | 0.001550 s | 9592 |

El codigo optimizado es aproximadamente **30000 veces mas rapido** y obtiene
exactamente el mismo resultado (9592 primos).

**Analisis de cProfile** (`profiling_optimizado.txt`): casi todo el tiempo se
concentra en la funcion `buscarPrimosOptimizado`, y dentro de ella las
operaciones de numpy (`ones`, `where`) son las q mas pesan, pero estan
optimizadas en C asi q igual son muy rapidas. En el codigo original el cuello
de botella era el bucle interno de verificacion de divisores.

**Graficos generados:**

- `grafico_comparativa_tiempos.png` : barras original vs optimizado
- `grafico_distribucion_tiempos.png` : torta con la distribucion del tiempo

## 4. Conclusiones

- Reducir el rango hasta la raiz cuadrada baja drasticamente las iteraciones
- NumPy permite operar sobre arrays enteros en una sola instruccion, mucho
  mas rapido q un bucle de Python
- cProfile sirve para saber exactamente q funcion consume mas tiempo antes de
  optimizar a ciegas
- Recomendacion: siempre revisar primero los bucles anidados, q suelen ser el
  primer punto a mejorar

## 5. Repositorio

Codigo subido a GitHub (ver `PASOS_GIT.md` para el detalle):

`https://github.com/USUARIO/optimizacion-primos`  *(reemplazar USUARIO)*

Rama de la optimizacion: **optimizacion-codigo**
