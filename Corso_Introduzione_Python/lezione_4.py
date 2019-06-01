'''
DATA TYPES

1.Strings
2.Numbers
3.Bool
4.List
5.Set
6.Dict
'''

variabile = 'testo variabile'
lista = [1, 2, 5, 6, variabile, 40, 'testo2', 56]

# stampa
print(lista)

'''
# esempio stampa ciclo
for i in lista:
    print(i)
'''

# SLICE (FARE A FETTE)
lista_spezzata_1 = lista[1:3]
print(lista_spezzata_1)

#PASSO
lista = [0,1,2,3,4,5,6,7,8,9,10]
print(lista[0:10:1])
print(lista[0:10:2]) # prende ogni 2 elementi
print(lista[1:10:3]) # prende ogni 3 elementi
print(lista[0:10:16])# nel caso di overflow, prende sempre il primo elemento

# IN = se è presente
'''
elemento = input("Scrivi un numero:\n")

if int(elemento) in lista:
    print('è nella lista')
else:
    print('non è nella lista')
'''

# Concatenare le liste usando l'operatore +
lista1 = [0,1,2,3,4,5]
lista2 = [5,6,7,8,9,10]
lista3 = lista1 + lista2
print(lista3)

#Operatore '*' ripetere gli elementi n volte
lista = [1,2,3]
output = lista *3
print(output)

#Lunghezza di una lista
lista = [0,1,2,3,4,5,6,7,8,9,10]
print(len(lista))

#Minimo e Massimo
lista = [0,1,2,3,4,5,6,7,8,9,10]
print('L\'elemento minimo è: ' + str(min(lista)))
print('L\'elemento massimo è ' + str(max(lista)))