# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
pc = randint(0,2)

if pc == 0:
     jogada_pc = 'PEDRA'
elif pc== 1:
     jogada_pc = 'PAPEL'
else:
     jogada_pc = 'TESOURA'
jogador = int(input(f'Suas opções: '
                     f'\n [0] - PEDRA'
                     f'\n [1] - PAPEL'
                     f'\n [2] - TESOURA'
                     f'\nDigite sua jogada: '))
if jogador == 0:
    jogada_jogador = 'PEDRA'
elif jogador == 1:
    jogada_jogador = 'PAPEL'
else:
    jogada_jogador = 'TESOURA'


print()
print('Processando jogada',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
obs = 0
if jogador == pc:
    resultado = 'EMPATE'
    obs = 'EMPATE'
elif jogador == 0 and pc == 2:
    resultado = 'JOGADOR GANHOU'
    obs = 'PEDRA AMASSA TESOURA'
elif jogador == 1 and pc == 0:
    resultado = 'JOGADOR GANHOU'
    obs = 'PAPEL COBRE PEDRA'
elif jogador == 2 and pc == 1:
    resultado = 'JOGADOR GANHOU'
    obs = 'TESOURA CORTA PAPEL'
elif jogador == 0 and pc == 1:
    resultado = 'PC GANHOU'
    obs = 'PAPEL COBRE PEDRA'
elif jogador == 1 and pc == 2:
    resultado = 'PC GANHOU'
    obs = 'TESOURA CORTA PAPEL'
elif jogador == 2 and pc == 0:
    resultado = 'PC GANHOU'
    obs = 'PEDRA AMASSA TESOURA'
print(f'RESULTADO FINAL: '
      f'\nPC: {jogada_pc}'
      f'\nJOGADOR: {jogada_jogador}'
      f'\nJOGADA: {obs}'
      f'\nVENCEDOR: {resultado}')

