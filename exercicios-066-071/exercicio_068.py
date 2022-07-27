# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.
from time import sleep
from random import randrange

titulo = ' JOGO DO PAR OU IMPAR '
titulo2 = ' RESULTADO '
print('='*90)
print(f'{titulo:-^90}')
print('='*90)

vitorias = jogada_jogador = 0


while True:
    if vitorias == 0:
        jogador = int(input('PC - Eai jogador par ou impar?'
                            '\nDigite 0 para par'
                            ' ou 1 para impar'
                            ': '))
        jogada_jogador = int(input('PC - Digite sua jogada(qunt.dedos): '))
        while jogador != 0 and jogador != 1:
            jogador = int(input('PC - Jogada inválida!'
                                ' Digite 0 para par '
                                'ou 1 para impar: '))
    else:
        jogador = int(input('PC - Parabéns jogador, vc venceu!!! Mas não desistirei tão fácil. '
                            '\nSó terminaremos quando eu te derrotar...'
                            ' Digite 0 para par'
                            ' ou 1 para impar'
                            ': '))
        jogada_jogador = int(input('PC - Digite sua jogada(qunt.dedos): '))

    while jogador!=0 and jogador!=1:
        jogador = int(input('PC - Jogada inválida!'
                            ' Digite 0 para par '
                            'ou 1 para impar: '))
    if jogador == 0:
        titulo_jogada_jogador = 'PAR'
        titulo_jogada_pc = 'IMPAR'

    elif jogador == 1:
        titulo_jogada_jogador = 'IMPAR'
        titulo_jogada_pc = 'PAR'


    jogada_pc = randrange(10)
    soma_resultado = jogada_jogador + jogada_pc

    if soma_resultado%2 == 0:
        resultado = 'PAR'
        if resultado == titulo_jogada_jogador:
            vitorias += 1
            vencedor = 'Jogador'
        elif resultado == titulo_jogada_pc:
            vencedor = 'PC'
    elif soma_resultado%2 == 1:
        resultado = 'IMPAR'
        if resultado == titulo_jogada_jogador:
            vitorias += 1
            vencedor = 'Jogador'
        elif resultado == titulo_jogada_pc:
            vencedor = 'PC'
    if vencedor!= 'Jogador':
        break
    sleep(1.5)
    print('\nPAR',end=' ')
    sleep(0.5)
    print('OU',end=' ')
    sleep(0.5)
    print('IMPAR?')
    sleep(1.5)
    print()
    print('='*90)
    print(f'{titulo2:-^90}')
    print(f'jogador pediu: {titulo_jogada_jogador }'
          f'  PC pediu: {titulo_jogada_pc }'
          f'\nJogada do Jogador: {jogada_jogador}'
          f' Jogada do PC: {jogada_pc}'
          f' Soma: {soma_resultado}'
          f'\nResultado final: {resultado}'
          f'\nVencedor: {vencedor}')

print('='*90)
print(f'{titulo2:-^90}')
print(f'jogador pediu: {titulo_jogada_jogador }'
      f'  PC pediu: {titulo_jogada_pc }'
      f'\nJogada do Jogador: {jogada_jogador}'
      f'  Jogada do PC: {jogada_pc}'
      f'  Soma: {soma_resultado}'
      f'\nResultado final: {resultado}'
      f'\nVencedor: {vencedor}')
if vitorias == 0:
    print('Que azar em jogador. Vc foi derrotado de primeira. Mais sorte da próxima!!!')
else:
    print(f'Parabéns jogador!!! Vc tem muita sorte. Obteve {vitorias} vitória(s) consecutiva(s)...')
