l = [5,2,1]
cant = int(input("Cantidad de €? "))
cambio = [0,0,0]
for i in range(len(l)):
    while cant >= l[i]:
        cant -= l[i]
        cambio[i] += 1
for i in range(len(cambio)):
    print(cambio[i], ' monedas de ', l[i], ' €')