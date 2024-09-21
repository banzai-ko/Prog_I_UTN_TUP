
def selection_sort(lista_numeros: list[int], modo: str):
    
    for indice in range(len(lista_numeros) - 1):
        indice_minimo = indice
        for sub_indice in range(indice + 1, len(lista_numeros)):
            if (modo == 'ASC' and lista_numeros[sub_indice] < lista_numeros[indice] or 
                modo == 'DES' and lista_numeros[sub_indice] > lista_numeros[indice]):
                indice_minimo = sub_indice
        
        if indice_minimo != indice:
            lista_numeros[indice], lista_numeros[sub_indice] =\
            lista_numeros[sub_indice], lista_numeros[indice]
            
    return lista_numeros


print(selection_sort([5,2,6,1], 'ASC'))