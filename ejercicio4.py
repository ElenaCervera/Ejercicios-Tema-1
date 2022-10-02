#Durante la planificación de un proyecto se han acordado una lista de tareas. 
# Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

#¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

#Sugerencia

#Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.

from collections import deque


tareas=[
    [5, "Lavar la ropa"],
    [3, "Ordenar"],
    [2, "Poner la mesa"],
    [1, "Cocinar"],
    [4, "Limpiar"],
    [6, "Leer"],
]
tareas.sort()
print(tareas)
cola=deque()
for tareasinnum in tareas:
    cola.append(tareasinnum[1])
for tareasinnum in cola:
    print(tareasinnum) 



