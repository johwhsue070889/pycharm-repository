# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
num = []
while True:
    numbers = int(input('Enter a number: '))
    if numbers not in num:
        num.append(numbers)
        print('Added value successfully...')
    else:
        print('Duplicate value! Will not be added to the list!!')
    exit = str(input('Do you want to add some more numbers?[Y/N]: ')).strip().upper()
    while exit != 'Y' and exit != 'N':
        exit = str(input('Invalid value! Do you really want to add some more numbers?[Y/N]: ')).strip().upper()
    if exit == 'N':
        break
print(f'\nValues entered: ',end='')
cont = 0
for n in num:
    cont += 1
    if cont != len(num):
        print(n,end=',')
    else:
        print(n, end='.')

order_numbers = sorted(num)
print(f'\nValues in ascending order: ',end='')
cont = 0
for n in order_numbers:
    cont+=1
    if cont != len(order_numbers):
        print(n,end=' -> ')
    else:
        print(n, end='.')
order_numbers = sorted(num,reverse=True)
print(f'\nValues in descending order: ',end='')
cont = 0
for n in order_numbers:
    cont+=1
    if cont != len(order_numbers):
        print(n,end=' <- ')
    else:
        print(n, end='.')
