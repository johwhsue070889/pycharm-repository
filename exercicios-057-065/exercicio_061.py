# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.
titulo = ' 10 TERMOS DE UMA PA COM WHILE '

print('='*40)
print(f'{titulo:-^40}')
print('='*40)
termo1 = int(input('O PRIMEIRO TERMO DA PA DESEJADA:'))
r = int(input('A RAZÃO DESSA PA: '))
c = 0
pa = 0
print()
print(f'OS 10 PRIMEIROS TERMOS DE UMA PA COM O 1º TERMO = {termo1} e RAZÃO = {r}:')
print('-'*65)
while c < 10:
    if c < 10:
        print(termo1,end=' -> ')
    else:
        print(termo1,end='')
    c += 1
    termo1 += r
print('FIM')