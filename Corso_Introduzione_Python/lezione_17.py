'''

CICLI
    WHILE
        FOR
        BREAK, CONTINUE
        RANGE
        FOR ELSE
    WHILE ELSE

'''

a = input('Inserisci un numero\n')
for el in range(0, int(a)):
    print(el)
    if el == 12:
        print('HAI VINTO')
        break
else:
    print('HAI PERSO')