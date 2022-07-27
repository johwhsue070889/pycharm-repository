# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.
maior = menor = 0
for c in range (1,6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if c == 1:
     maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print()
print(f'Maior peso registrado: {maior} Kg.'
      f'\nMenor peso registrado: {menor} Kg.')