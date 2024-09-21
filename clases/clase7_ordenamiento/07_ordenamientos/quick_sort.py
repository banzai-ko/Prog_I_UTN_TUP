
def quick_sort(lista_numeros: list[int], modo: str) -> list[int]:
    
    if len(lista_numeros) < 2:
        return lista_numeros
    
    pivot = lista_numeros.pop()
    mas_chicos = []
    mas_grandes = []
    
    for numero in lista_numeros:
        if numero <= pivot:
            mas_chicos.append(numero)
        else:
            mas_grandes.append(numero)
    
    if modo == 'ASC':
        return quick_sort(mas_chicos, modo) + [pivot] + quick_sort(mas_grandes, modo)
    elif modo == 'DES':
        return quick_sort(mas_grandes, modo) + [pivot] + quick_sort(mas_chicos, modo)


print(quick_sort([5,2,6,1], 'ASC'))