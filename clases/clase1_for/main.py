suma_edades = 0
cantidad_vueltas = 3

# [1;6)

for vuelta in range(cantidad_vueltas):

    print(f'{vuelta}° vuelta del for')
    edad_actual = None
    vuelta_while = 0

    while not edad_actual or not edad_actual.isdigit():
        vuelta_while += 1
        print(f'{vuelta_while}° vuelta While')
        edad_actual = input(f'Ingrese la {vuelta + 1}° edad: ')
    edad_actual_int = int(edad_actual)

    if edad_actual_int == 34:
        break

    # sumo edades pares
    suma_edades += edad_actual_int

print(f'La suma de {cantidad_vueltas} edades es: {suma_edades}')
