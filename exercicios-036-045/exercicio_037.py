# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para
# o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
n1 = int(input('Digite um valor para conversão de base: '))
n2 = int(input('\nEscolha qual conversão deseja realizar:'
               '\n\n [1] Converter para BINÁRIO'
               '\n [2] Converter para OCTAL'
               '\n [3] Converter para HEXADECIMAL'
               '\n\nDigite aqui sua opção: '))
if n2 == 1:
    n3 = 'Binário'
    convertido = bin(n1)
elif n2 == 2:
    n3 = 'Octal'
    convertido = oct(n1)
else:
    n3 = 'Hexadecimal'
    convertido = hex(n1)
sleep(0.5)
print()
print('Convertendo',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
print()
print(f'Opção escolhida: {n2}'
      f'\nConversão para: {n3}'
      f'\nNúmero digitado: {n1}'
      f'\nResultado: {n1} em {n3} é {convertido[2:]}!')
