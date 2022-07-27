# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla.
titulo = ' SORTEIO NUMÉRICO '
print('='*45)
print(f'{titulo:-^45}')
print('='*45)
from random import randrange
n = (randrange(1,20),randrange(1,20),randrange(1,20),randrange(1,20),randrange(1,20))
print('NÚMEROS SORTEADOS: ',end='')
cont = maior = menor=0
for c in range(0,5):
    if cont ==0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        elif n[c] < menor:
            menor = n[c]
    if cont < 4:
        print(n[c],end=', ')
    else:
        print(n[c], end='.')
    cont+=1
print(f'\nMAIOR VALOR NA SEQUÊNCIA: {maior}')
print(f'MENOR VALOR NA SEQUÊNCIA: {menor}')
