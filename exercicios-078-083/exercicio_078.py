# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em
# uma lista.No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
n = []
maior = menor = 0
for c in range (0,5):
     n.append(int(input(f'Digite um n° para o indice {c}° da lista: ')))
     if c == 0:
         maior = menor = n[c]
     else:
         if n[c] > maior:
             maior = n[c]
         elif n[c] < menor:
             menor = n[c]
print(f'\nValores inseridos na lista: ',end='<...')
cont = 0
for v in n:
    if cont < 4:
        print(v,end='...')
    else:
        print(v, end='...>')
    cont+=1
print(f'\nMaior valor na lista = {maior},inserido no(s) índice(s): ',end='<...')
for pos,c in enumerate(n):
        if c == maior:
            print(pos,end='...')
print('', end='>')
print(f'\nMenor valor na lista = {menor},inserido no(s) índice(s): ',end='<...')
for pos,c in enumerate(n):
        if c == menor:
            print(pos,end='...')
print('', end='>')
