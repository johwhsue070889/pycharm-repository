# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
from time import sleep
primeiro = int(input('Digite um valor: '))
segundo = int(input('Digite outro valor: '))

sleep(0.5)
print()
print('Comparando',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
print(f'1º valor digitado: {primeiro}'
      f'\n2° valor digitado: {segundo}')

if segundo > primeiro:
    maior = 'segundo'
    print(f'Entre os valores digitados o {maior} é maior!')
elif primeiro > segundo:
    maior = 'primeiro'
    print(f'Entre os valores digitados o {maior} é maior!')
else:
    maior = 'iguais'
    print(f'Entre os valores digitados não existe maior,ambos são {maior}!')


