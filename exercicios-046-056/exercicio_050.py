# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s_pares = 0
s_impares = 0
s_total = 0
cont_pares = 0
cont_impares = 0
cont_total = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º número: '))
    s_total+=n
    cont_total +=1
    if n%2 == 0:
        s_pares+=n
        cont_pares+=1
    else:
        s_impares+=n
        cont_impares+=1
print(f'Quantidade de números pares digitados: {cont_pares}. '
      f'\nSoma dos valores pares na sequência: {s_pares}.'
      f'\nQuantidade de números impares digitados: {cont_impares}.'
      f'\nSoma dos valores impares na sequência: {s_impares}.'
      f'\nQuantidade total de números digitados: {cont_total}.'
      f'\nSoma total de pares e impares: {s_total}.')
