#Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares y la segunda con los números impares.

#Por ejemplo:

#pares, impares = separar([6,5,2,1,7])

#print(pares)

#print(impares)

#[2, 6]

#[1, 5, 7]

#Sugerencia

#Para ordenar una lista automáticamente puedes utilizar el método .sort().


numeros=[5,33,4,74,69,14,25,91,37,6]
def par_impar (numeros):
    pares=[]
    impares=[]
    
    print("La lista de números es:", numeros)
    for i in numeros:
        if i%2 == 0:
            pares.append(i)
        else:
                impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares

pares, impares=par_impar(numeros)
print("Los números pares de la lista son:", pares)
print("Los números impares de la lista son:", impares)    

