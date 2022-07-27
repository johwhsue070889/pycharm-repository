# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
from time import sleep

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
sleep(0.5)
print()
print('Calculando',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
print(f'Resultado final:'
      f'\nNota 1: {n1:.1f}'
      f'\nNota 2: {n2:.1f}'
      f'\nMédia final: {m:.1f}'
      f'\nStatus: ',end='')
if m < 5.0:
    print('Aluno REPROVADO!')
elif m < 7.0:
    print('Aluno em RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')