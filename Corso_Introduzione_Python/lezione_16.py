'''

CICLI
    WHILE
        FOR
        BREAK, CONTINUE
        RANGE
    FOR ELSE
    WHILE ELSE

'''

lista = [1, 2, 3, 3, 4, 5, 5, 6]

for l in lista:
    if l == 2:
        continue # salta il ciclo e va avanti
    if l == 5:
        break #blocca l'esecuzione del programma
    print(l)
