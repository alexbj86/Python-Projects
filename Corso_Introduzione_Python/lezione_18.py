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
a = int(a)

while a < 10:
    print(a)
    if a == 5:
        print('CINQUE')
        break
    a += 1
else:
    print('ALTRO')