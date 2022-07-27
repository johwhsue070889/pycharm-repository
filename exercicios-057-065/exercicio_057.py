# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Informe seu sexo[M/F]: ')).strip()[0]
while s!= 'M' and s != 'm'and s != 'F' and s != 'f':
    s = str(input('Dado inválido informado.Digite novamente seu sexo[M/F]: '))
if s in 'Mm':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
