# Exercício Python 081: Crie um programa que vai ler vários números e
# colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

n = []
while True:
    n.append(int(input('Enter a value: ')))
    exit = str(input('Do you wish to continue?[Y/N]: ')).strip().upper()
    while exit!='Y' and exit!='N':
        exit = str(input('Invalid value!Are you sure you want to continue??[Y/N]: ')).strip().upper()
    if exit == 'N':
        break
print(f'\nA) Quant. números inseridos na lista: {len(n)} números.')
new_order = sorted(n,reverse=True)
print(f'B) Valores inseridos na lista, ordenados de forma decrescente:',end='')
cont = 0
for num in new_order:
    cont+=1
    if cont != len(new_order):
        print (num,end=',')
    else:
        print(num, end='.')
print(f'\nC) Valor 5 está na lista: ',end='')
if 5 in new_order:
    print('Sim! Há um valor 5 inserido na lista!')
else:
    print('Não! Não há valor 5 inserido na lista!')


