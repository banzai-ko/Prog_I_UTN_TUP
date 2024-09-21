from funciones import *

if __name__ == "__main__":
    mostrar_opciones()
    
    seleccion = entrada("Ingrese una opcion: ", 1, 2)
    if seleccion == 1:
        menu_multiplicar()
    elif seleccion == 2:
        menu_test()
        