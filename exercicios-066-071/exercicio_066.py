# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# elas (desconsiderando o flag).
n = c = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    c+=1
    soma+=n
print(f'\nForam digitados {c} números.'
      f'\nE a soma desses números é {soma}.')

