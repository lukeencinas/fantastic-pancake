#1) e1 = ["F. de Computadores", "Visualizacion","Fisica","Quimica", "Historia", "Lengua"]
# print(e1)

#2) e2 = ["F. de Computadores", "Visualizacion","Fisica","Quimica", "Historia", "Lengua"]
# for i in e2:
  #  print("Yo estudio: "+i)

#3) e3 = ["F. de Computadores", "Visualizacion","Fisica"]
# nota = []
# for i in e3:
  #  nota.append(input('¿Que has sacado en '+ i + '? '))
# for i in range(len(e3)):
 #   print ("En la asignatura ",e3[i]," Has sacado ",nota[i])


#4) e4 = []
# for i in range(6):
  #  e4.append(int(input("¿Cuales son los numeros de la loteria? ")))
# e4.sort()
# print("Los numeros en orden son: "+ str(e4))



m1 = ((1,2,3),(4,5,6))
m2 = ((-1,0),(0,1),(1,1))
resultado = [[0,0],[0,0]]

for i in range(len(m1)):  #recorre la primera matriz
    for j in range(len(m2[0])): #recorre m2 empezando desde el principi
        for k in range(len(m2)): # recorre m2
            resultado[i][j] += m1[i][k] * m2[k][j] # Multiplica elementos de filas por columnas
for i in range(len(resultado)): # Transforma en tuplas el resultado
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)
for i in range(len(resultado)):
    print(resultado[i])