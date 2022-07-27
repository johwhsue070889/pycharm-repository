# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
idade = maior_18 = homens = mulheres_menores_20 = 0
cont = 1
titulo = ' CADASTRE A 1° PESSOA '
print('='*25)
print(f'{titulo}')
while True:
    print('=' * 25)
    idade = int(input('Digite sua idade: '))
    if idade >=18:
        maior_18+=1
    sexo = str(input('Digite seu sexo[M/F]: ')).strip()[0]
    while sexo!= 'M' and sexo!= 'm' and sexo!= 'F' and sexo!= 'f':
        sexo = str(input('Valor inválido! Digite seu sexo[M/F]: ')).strip()[0]
    if sexo == 'M' or sexo== 'm':
        homens+=1
    else:
        if idade < 20:
            mulheres_menores_20 +=1
    sair = str(input('Deseja realizar mais algum cadastro[S/N]: ')).strip()[0]
    while sair != 'S' and sair != 's' and sair != 'N' and sair != 'n':
        sair = str(input('Valor inválido! Deseja realmente realizar mais algum cadastro[S/N]: ')).strip()[0]
    if sair == 'N' or sair == 'n':
        break
    cont += 1
    print('=' * 25)
    print(f' CADASTRE A {cont}° PESSOA ')
titulo2 = ' RELATÓRIO FINAL '
print()
print('='*50)
print(f'{titulo2:-^50}')
print('='*50)
print(f'PESSOAS MAIORES DE 18 ANOS: {maior_18} PESSOA(S).'
      f'\nQUANTIDADE DE HOMENS CADASTRADOS: {homens} HOMEN(S).'
      f'\nQUANTIDADE DE MULHERES COM MENOS DE 20 ANOS: {mulheres_menores_20} MULHER(ES).')
