'''

OPERATORI

#OPERATORI DI CONFRONTO

'''


a = 10
b = 20

#uguaglianza
print(a == b)

#maggione e minore
print(a > b)
print(a < b)

#diverso
print(a != b)



#maggiore minore
a = 10
b = 10
print(a >= b)
print(a <= b)

#programmino
elem1 = input('scrivi un numero \n')
elem2 = input('scrivi un numero \n')

if int(elem1) < int(elem2):
    print('Il numero è minore')
elif int(elem1) > int(elem2):
    print('Il numero è maggiore')
else:
    print('Il numero sono uguali')
