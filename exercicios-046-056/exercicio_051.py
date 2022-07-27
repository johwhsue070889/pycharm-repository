# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
titulo = '10 termos de uma PA'
print('='*40)
print(f'{titulo:^40}')
print('='*40)
termo_1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
dec = termo_1 + (10 - 1) * r

for c in range(termo_1,dec+r,r):
    print(f'{c}',end=' -> ')
print('fim')