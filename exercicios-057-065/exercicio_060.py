# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
from time import sleep
titulo = ' CALCULO DO FATORIAL '
titulo2 = ' RESPOSTA '
print("="*90)
print(f'{titulo:-^90}')
print("="*90)
n = int(input('Digite um número que deseje o fatorial: '))
f = 1
print()
sleep(1)
print(f'{titulo2:^90}')
sleep(1)
print(f'{n}!',end=' = ')
while n > 0:
    if n>1:
        sleep(1)
        print(n,end=' x ')
    else:
        print(n,end=' = ')
    f *= n
    n -= 1
sleep(1)
print(f)
