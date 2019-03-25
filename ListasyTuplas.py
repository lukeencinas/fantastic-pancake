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