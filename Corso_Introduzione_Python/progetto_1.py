'''

ARCHIVIO

1. Inserire un libro

'''

archivio = []

condizione = True
while condizione == True:
    elem = input('Scrivi il nome del libro: \n')
    archivio.append(elem)
    print('IL NOSTRO ARCHIVIO:\n')
    print(archivio)
    if elem == 'x':
        condizione = False