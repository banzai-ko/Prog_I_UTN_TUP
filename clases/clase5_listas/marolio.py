""" 
Clase 5 Listas
  Ejemplo de uso de listas
 """

lista_marolio = [
    "mate", "café", "harina", "palmitos", "yerba", "mermelada", "cacao", "picadillo",
    "paté", "caballa", "arroz", "arvejas", "sardinas", "atún", "choclo", "lentejas"
]
lista_vacia = []
# otra forma de crear una lista vacía, al linter mucho no le gusta
otra_lista_vacia = list()

lista_con_ceros = [0] * 6 # 0,0,0,0,0,0


for indice in range(len(lista_marolio)):
    print('posicion: ', indice, '| dato', lista_marolio[indice])


for nombre in lista_marolio:
    print(nombre)


print(lista_marolio[-16])
print(len(lista_marolio))


print(hex(id(lista_marolio)))
lista_marolio.append("galletas_naranja")
print(len(lista_marolio))
print(hex(id(lista_marolio)))
