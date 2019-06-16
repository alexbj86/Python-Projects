'''

OPERATORI

#OPERATORI BOOLEANI

'''

a = 10
b = 20
3
#and, or, not

#programmino che dimostra il funzionamento di and, or, not
elem1 = input('scrivi i1 numero 1: \n')
elem2 = input('scrivi il numero 2: \n')
elem3 = input('scrivi il numero 3: \n')

if int(elem1) > 0 and int(elem2) < 20:
    print('caso uno')
elif int(elem1) > 10 or int(elem2) > 20:
    print('caso due')
elif not elem3:
    print('caso tre')


