
def bubble_sort(lista_numeros: list[int], modo: str): # ASC | DES
    
    for indice in range(len(lista_numeros) - 1):
        for sub_indice in range(indice + 1, len(lista_numeros)):
            
            if (modo == 'ASC' and lista_numeros[indice] > lista_numeros[sub_indice] or 
                modo == 'DES' and lista_numeros[indice] < lista_numeros[sub_indice]):
                lista_numeros[indice], lista_numeros[sub_indice] =\
                lista_numeros[sub_indice], lista_numeros[indice]

    return lista_numeros


print(bubble_sort([5,2,8,15], 'DES'))
# print(bubble_sort([5,2,8], 'ASC'))