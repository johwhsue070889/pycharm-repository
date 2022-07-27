# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = c = soma = 0
while n!=999:
    n = int(input('Digite um número pra continuar e ser somado ou 999 para parar: '))
    if n != 999:
        c += 1
        soma += n
print(f'\nQuantidade de nº(s) digitado(s): {c} números'
      f'\nSoma desses nº(s) = {soma}')
