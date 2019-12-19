
# nombrediccionario = {a1:a,...}

dic1 = {"Juan":"Ingeniero","Jose":"Medico","Jorge":"Abogado"}
print(dic1)

dic2 = {"Juan":23,"Jose":20,"Jorge":26}
print(dic2)

#Buscar por posicion el valor del parametro en el diccionario
print(dic1["Juan"])
print(dic2["Jorge"])

#Combinar la Lista con el diccionario
lis = ["Dell","Lenovo","Sony VAIO","Toshiba"]
dic3 = {lis[0]:"Laptop",lis[1]:"All one",lis[2]:"Equipo",lis[3]:"Pc"}

print(dic3)
print(dic3["Lenovo"])

#Combinar la Tupla con el diccionario
tup = "HP","Samsung","Sony","Huawei"
dic4 = {tup[0]:"Impresora",tup[1]:"Tablet",tup[2]:"Equipo",tup[3]:"celular"}

print(dic4["Sony"])