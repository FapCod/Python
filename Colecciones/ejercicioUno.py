print("eliminar elementos repetidos de una lista")
lista=[1,2,3,"Frank",2,2,1,"Frank",3]
#Una forma
'''conjunto = set(lista)
lista= list(conjunto)'''
#Segunda forma
lista =list(set(lista))
print(lista)
