# Exercício Python 082: Crie um programa que vai ler vários números e colocar em
# uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

n = []
odd = []
even = []

while True:
    n.append(int(input('Enter a value: ')))
    exit = str(input('Do you wish to continue?[Y/N]: ')).strip().upper()
    while exit!= 'Y' and exit!='N':
        exit = str(input('Invalid value!Are you sure you want to continue??[Y/N]: ')).strip().upper()
    if exit == 'N':
        break
for num in n:
    if num%2==0:
        odd.append(num)
    else:
        even.append(num)
order_full_list = sorted(n)
order_odd = sorted(odd)
order_even = sorted(even)
print('\nA) Lista completa:',end=' ')
cont = 0
for num in n:
    cont+=1
    if cont!= len(n):
        print(num,end=',')
    else:
        print(num,end='.')

print('\nB) Lista completa ordenada (ordem crescente):',end=' ')
cont = 0
for num in order_full_list:
    cont+=1
    if cont!= len(order_full_list):
        print(num,end=',')
    else:
        print(num,end='.')

print('\nC) Lista somente com pares:',end=' ')
cont=0
for num in odd:
    cont+=1
    if cont != len(odd):
        print(num,end=',')
    else:
        print(num,end='.')

print('\nD) Lista ordenada dos pares(ordem crescente):',end=' ')
cont = 0
for num in order_odd:
    cont+=1
    if cont!= len(order_odd):
        print(num,end=',')
    else:
        print(num,end='.')

print('\nE) Lista somente com impares:',end=' ')
cont=0
for num in even:
    cont+=1
    if cont != len(even):
        print(num,end=',')
    else:
        print(num,end='.')

print('\nF) Lista ordenada dos impares(ordem crescente):',end=' ')
cont = 0
for num in order_even:
    cont+=1
    if cont!= len(order_even):
        print(num,end=',')
    else:
        print(num,end='.')

