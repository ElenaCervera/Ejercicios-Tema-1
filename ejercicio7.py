#Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar
#  y mostrar este mensaje en su lugar:

#Error: Imposible añadir elementos duplicados => [elemento].
#Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

#Sugerencia

#Puedes utilizar la sintaxis "elemento in lista"

elementos=[10, -2, "Hola"]

def agregar_una_vez(lista, elemento):
  lista=[5,3,7,1,8]
  elemento=2
  print(lista)
  if len(lista)==0:
        lista.append(elemento)
        print(lista)
  else:
    for el in lista:
        if el == elemento:
            print("Error: Imposible añadir elementos duplicados => [elemento].")
        else:
          lista.append(elemento) 
          break
  print(lista)











            
    



    
