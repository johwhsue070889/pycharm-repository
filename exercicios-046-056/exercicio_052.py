# Exercício Python 052: Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
print(f'\nNúmero digitado:'
      f'\n{n}'
      f'\nSequência númerica de 1 até {n}: ',end='')
print()
for c in range(1,n+1):
    print(c,end=' ')
print()
print(f'Números da sequência divisíveis por {n}: ',end='')
print()
cont=0
for c in range(1,n+1):
    if n%c == 0:
        cont+=1
        print(c,end=' ')
print(f'\nConclusão:'
      f'\nO número {n} foi divisível {cont} veze(s) na sequência númerica.'
      f'\nPortanto, o número {n} ',end='')
if cont > 2 or cont< 2:
    print('não é um número primo!')
else:
    print('é um número primo!')

