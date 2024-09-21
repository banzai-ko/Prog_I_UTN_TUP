def entrada(text, limit_i, limit_s) -> int:
    '''_summary_ Entrada y validación de datos

    Returns:
        int: _description_ Devuelve la seleccion si es un valor numerico,
        si no pide reingreso
    '''

    seleccion = input(text)
    while int(seleccion) > limit_s or int(seleccion) < limit_i or not seleccion.isdigit():
        seleccion = input('Ingrese una opcion: ')

    return int(seleccion)


def cargar_matriz(filas: int, columnas: int) -> list[list]:
    '''Carga una matriz de dimensiones dadas solicitando al usuario los elementos.

    Args:
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.

    Returns:
        list[list]: Matriz cargada con los elementos ingresados por el usuario.
    '''
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = (input(f'Ingrese el elemento [{i + 1}, {j + 1}]: '))
            while not elemento.isdigit():
                elemento = (
                    input(f'Ingrese el elemento (solo entrada numérica)[{i + 1}, {j + 1}]: '))
            fila.append(int(elemento))
        matriz.append(fila)
    return matriz


def multiplicar_matrices(matriz_1: list[list], matriz_2: list[list]) -> list[list]:
    '''_summary_ Multiplica 2 matrices

    Args:
        matriz_1 (list[list]): _description_ Parámetro de entrada, mat. A
        matriz_2 (list[list]): _description_ Parámetro de entrada, mat B

    Returns:
        list[list]: _description_ Devuelve matriz C
    '''
    matriz_3 = []
    for fila in range(len(matriz_1)):
        lista_mult = []
        for columna in range(len(matriz_1[fila])):
            suma = 0
            for i in range(len(matriz_1[fila])):
                suma += (matriz_1[fila][i] * matriz_2[i][columna])
            lista_mult.append(suma)
        matriz_3.append(lista_mult)
    return matriz_3


def verificar_dimensiones(matriz_a: list[list], matriz_b: list[list]) -> bool:
    '''Verifica si las dimensiones de las matrices son compatibles para multiplicar

    Args:
        matriz_1 (list[list]): Matriz A.
        matriz_2 (list[list]): Matriz B.

    Returns:
        bool: Si es posible multiplicar devuelve V, si no F.
    '''
    return len(matriz_a[0]) == len(matriz_b)


def mostrar_matriz(matriz: list[list]) -> None:
    '''Muestra una matriz en la consola.

    Args:
        matriz (list[list]): Matriz a mostrar.
    '''
    for fila in matriz:
        print(' '.join(map(str, fila)))


def test_multiplicar_matrices():
    '''
    Test para multiplicador de matrices
    Con resultados pre-definidos    
    Imprime por pantalla el resultado del test
    Args:
        None

    Returns:
        None
    '''
    matriz_1 = [
        [1, 2],
        [3, 4]
    ]

    matriz_2 = [
        [5, 6],
        [7, 8]
    ]

    expected_result = [
        [19, 22],
        [43, 50]
    ]
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    result = multiplicar_matrices(matriz_1, matriz_2)
    mostrar_matriz(result)
    if result == expected_result:
        print(f'Test {GREEN}PASSED{RESET}')
    else:
        print(f'Test {RED}FAILED:{RESET} Expected {
              expected_result}, but got {result}')


def mostrar_opciones() -> None:
    '''Muestra las opciones del menú.'''
    print('ELEGIR OPCIÓN:')
    print('1. Multiplicar matrices')
    print('2. TEST: Multiplicar matrices')


def menu_multiplicar() -> None:
    '''
    Menu wrapper para la multiplicación de matrices.
    '''
    print('Multiplicar matrices')
    print('Cargar matrices')
    
    print('Matriz A')
    filas_a = entrada('Filas: 1-10: ', 1, 10)
    columnas_a = entrada('Columnas: 1-10: ', 1, 10)
    matriz_a = cargar_matriz(filas_a, columnas_a)

    print('Matriz B')
    filas_b = entrada('Filas: 1-10: ', 1, 10)
    columnas_b = entrada('Columnas: 1-10: ', 1, 10)
    matriz_b = cargar_matriz(filas_b, columnas_b)

    if not verificar_dimensiones(matriz_a, matriz_b):
        print('No es posible multiplicar las matrices ingresadas. \
              La cantidad de filas de la Matriz A no es igual a la \
              cantidad de columnas de la Matriz B')
        return

    print('Resultado:')
    matriz_resultado = multiplicar_matrices(matriz_a, matriz_b)
    mostrar_matriz(matriz_resultado)


def menu_test() -> None:
    '''Menu wrapper para el test de multiplicación de matrices.'''
    print('TEST: Multiplicar matrices')
    test_multiplicar_matrices()

