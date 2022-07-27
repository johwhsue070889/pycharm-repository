# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
# n = int(input('A sequência de Fibonacci de: '))
# a, b = 0, 1
# while a < n:
#     print(a, end=',')
#     a, b = b, a+b
# print('FIM')
titulo = ' SEQUÊNCIA DE FIBONACCI '
print('>'*30)
print(f'{titulo:^30}')
print('<'*30)
termos = int(input('DIGITE AQUI QUANTOS TERMOS DESEJA DA SEQUÊNCIA DE FIBONACCI: '))
cont = 0
n1 = 0
n2 = 1
soma = 0
print()
while cont < termos:
    cont+=1
    print(soma,end=' -> ')
    soma = n2 + n1
    n2 = n1
    n1 = soma
print('FIM')






















