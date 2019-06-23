'''

CICLI
    FOR
        WHILE
    BREAK, CONTINUE
    FOR ELSE
    WHILE ELSE

'''

#CICLO WHILE

condizione = True

# es. si interrompe quando si inserisce un numero pari
while condizione == True:
    print('VERA')
    elem = input('Inserisci un numero\n')
    if int(elem)%2 == 0:
        condizione = False
        print('FINE DEL PROGRAMMA')