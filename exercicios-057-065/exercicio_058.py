# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.
from random import randrange
from time import sleep
titulo = 'JOGO DA ADVINHAÇÃO'
titulo2 = 'PC - Eai jogador! Que tal jogarmos um pouco!? ' \
         '\nPC - Pensei em um número entre 0 e 10.' \
          '\nPC - Eai,qual o seu palpite?'
print('='*90)
print(f'{titulo:^90}')
print('='*90)
print(f'{titulo2:<21}')
pc = randrange(0,10)
n = int(input('PC - Digite aqui (nº entre 0 e 10): '))
print(f'Seu número: {n}')
print()
sleep(0.2)
print('PROCESSANDO', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
cont = 1
print()
while pc!= n:
    cont += 1
    if pc > n:
        print('PC - Vc errou! Chute muito baixo.Tente novamente!')
    else:
        print('PC - Vc errou! Chute muito alto.Tente novamente!')
    n = int(input('Novo chute: '))
    print(f'Seu número: {n}')
    print()
    sleep(0.2)
    print('PROCESSANDO', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print()
titulo = 'RESULTADO FINAL'
print('='*60)
print(f'{titulo:^60}')
print('='*60)
print()
print(f'PC - Parabéns jogador !!!'
      f'\nPC - Vc acertou na {cont}º tentiva.')

