# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range (10,-1,-1):
    sleep(1)
    print(c)
print()
for c in range (0,2):
    sleep(1)
    print('Bum!',end=' ')
sleep(1.5)
print('Pooowww!!!')