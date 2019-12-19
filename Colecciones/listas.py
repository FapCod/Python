print("Creacionn de listas")
lista = []

#agregar al final de la lista
lista.append(6)
#lista.append("Frank")
#agregar en un lugar especifico con indice
lista.insert(2,5)
#agregar un conjunto de valores al final de la lista
lista.extend([7,8,9])

#Buscar en la lista
print(3 in lista)#devuelve boolean
print(lista.index(6))#te retorna el indice del valor ingresado
print(lista.count(2))#cuantas veces aparece el valor dado

#eliminar
#lista.pop()#elimina el ultimo valor
#lista.pop(3)#elimina elvalor que esta en el indice
#lista.remove(5)#elimina el valor enviado 5
#lista.clear()#elimina toda la lista
#Ordenar lista
lista.sort() #ordenade manera ascendente
lista.sort(reverse=True)# ordena de manra descendente



print(len(lista))
print(lista[0])
print(lista)
