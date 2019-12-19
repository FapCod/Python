print("Grpos de elemetso desordenados pero no pueden aver dos valores  iguales")


conjunto={1,2,3,4,5}
conjunto2={5,6,7,8,9,10}
#unuion de conjuntos
conjunto3= conjunto | conjunto2
print(conjunto3)
#Interseccion de conjutos (elementos en comun)
conjunto3= conjunto & conjunto2
print(conjunto3)
#Diferencia de conjuntos
conjunto3= conjunto - conjunto2#elementos de A que no esten en B
print(conjunto3)
#Diferencia simetrica
conjunto3 = conjunto ^ conjunto2
print(conjunto3)#elementos en A y B pero que no esten en ambos conjuntos




