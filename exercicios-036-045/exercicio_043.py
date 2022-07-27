# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
from time import sleep
print('Digite a seguir seu peso e altura para calculo do IMC:')
peso = float(input('Peso(xx.x):Kg '))
altura = float(input('Altura(x.xx): '))
massa = peso/pow(altura,2)
print()
print('Avaliando',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
if massa <18.5:
    imc = 'abaixo do Peso'
elif massa < 25.1:
    imc = 'no peso Ideal'
elif massa < 29.1:
    imc = 'com sobrepeso'
elif massa < 41:
    imc = 'com obesidade'
else:
    imc = 'com obesidade Mórbida'
print(f'Resultado da avaliação:'
      f'\nPeso atual: {peso} Kg'
      f'\nAltura: {altura} metros'
      f'\nIMC calculado: {massa:.1f}'
      f'\nConclusão: Usuário {imc}')



