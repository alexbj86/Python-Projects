'''

ARCHIVIO

1. Inserire un libro
2. Inserire i valori in un DIZIONARIO {Dante: La Divina Commedia}

'''

archivio = {}
condizione = True

while condizione == True:
    chiave = input('Scrivi l\'autore del libro: \n')
    archivio[chiave] = []

    valore = input('Scrivi il nome del libro: \n')
    archivio[chiave].append(valore)

    print('IL NOSTRO ARCHIVIO:\n' + str(archivio))

    if chiave == 'x':
        condizione = False

