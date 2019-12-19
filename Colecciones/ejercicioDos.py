'''lista1 = [1,2,3,"Frank",4,5,6,7,8]
lista2 = [2,3,"Antonio",6,7,8,9,10]
lista1=set(lista1)
lista2=set(lista2)
print("Listas de palabras que aparecen en las dos listas:")
print(lista1|lista2)
print("Lista de palabras que aparecen en la primera lista,pero no en la segunda")
print(lista1-lista2)
print("Lista de palabras que aparecen en la seguda lista, pero no n la primera")
print(lista2-lista1)
print("Lista de palabras que aparecen en ambas listas")
print(lista1&lista2)'''
lista1 = [1,2,3,"Frank",4,5,6,7,8]
lista2 = [2,3,"Antonio",6,7,8,9,10]
a=set(lista1)
b=set(lista2)
union = list(a|b)
soloA = list(a-b)
soloB = list(b-a)
interseccion = list(a&b)
print("Listas de palabras que aparecen en las dos listas:")
print(union)
print("Lista de palabras que aparecen en la primera lista,pero no en la segunda")
print(soloA)
print("Lista de palabras que aparecen en la seguda lista, pero no n la primera")
print(soloB)
print("Lista de palabras que aparecen en ambas listas")
print(interseccion)
