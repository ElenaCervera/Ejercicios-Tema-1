#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
# pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

def elementos_repetidos(lista_a, lista_b):
    lista_elementos_repetidos=[]
    for i in lista_a:
        for j in lista_b:
            if i == j:
                lista_elementos_repetidos.append(i)
    print(lista_elementos_repetidos)   
elementos_repetidos(lista_1, lista_2)    


      

