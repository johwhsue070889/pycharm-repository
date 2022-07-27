# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
titulo = ' ANÁLISE DE DADOS NUMA TUPLA '
titulo2 = 'NÚMEROS INSERIDOS NA TUPLA:'
titulo3 = 'QUANT. DE VEZES QUE O N° 9 APARECE NA TUPLA:'
titulo4 = 'QUAL POSIÇÃO APARECE O 1° N°3 NA TUPLA:'
titulo5 = 'QUEM SÃO OS NÚMEROS PARES NA TUPLA:'
titulo6 = 'CONCLUSÃO'
print('='*45)
print(f'{titulo:-^45}')
print('='*45)
n = (int(input('Digite o 1° Valor: ')),
     int(input('Digite o 2° Valor: ')),
     int(input('Digite o 3° Valor: ')),
     int(input('Digite o 4° Valor: ')))
print('='*90)
print(f'{titulo6:-^90}')
print('='*90)
print(f'{titulo2}',end=' ')
cont = 0
for c in n:
    if cont < 3:
     print(c,end=',')
    else:
        print(c,end='.')
    cont+=1
print(f'\n{titulo3}{n.count(9)} VEZ(ES) ')
cont = 0
for c in n:
     if c == 3:
      cont= 1
      print(f'{titulo4}{n.index(3)+1}° POS  ')
if cont == 0:
    print(f'{titulo4} N° 3 NÃO FOI DIGITADO! ')
print(f'{titulo5}',end=' ')
cont = 0
for pos, c in enumerate(n) :
    if c%2 ==0 :
      cont += 1
      print(f'N°{c} NA {pos+1}° POS ',end=', ')
    elif cont< 1:
        print('', end='. ')
