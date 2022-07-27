# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
s=0
quant = 0
for c in range (1,501,2):
   if c%3==0:
       quant+=1
       s+=c
print(f'Quantidade de números inteiros multiplos de 3 no intervalo entre 1 e 500: {quant} valores.'
      f'\nSoma total entre todos esses números: {s}.')