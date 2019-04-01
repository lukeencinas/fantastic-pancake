#simbolos = {'Euro':'€','Dollar':'$','Yen':'¥'}
#pregunta = input('Introduce una divisa (No simbolo) ')
#if pregunta in simbolos:
#    print(simbolos.get(pregunta)," Esta dentro.")
#else: 
#    print(pregunta," No esta. ")


lista = {}
lista['name'] = input("Cual es tu nombre? ")
lista['Telefono'] = input("Cual es tu telefono? ")
lista['Direccion'] = input("Cual es tu direccion? ")

print("Tu nombre es: " + lista.get('name')+ " que vive en: "+ lista.get('Direccion')+ " con nº de telefono ", lista.get('Telefono'))

