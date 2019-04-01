word = list(input('Introduce la palabra a adivinar: '))
failures = 0
while word and failures < 5:
    letter = input('Introduce una letra: ')
    if letter in word:
        print('Acierto')
        word.remove(letter)
    else:
        print('Fallo')
        failures += 1
if failures == 5:
    print('Perdiste')
else:
    print('Ganaste') 