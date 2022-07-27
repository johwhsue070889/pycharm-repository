# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO',
'SEIS','SETE','OITO','NOVE','DEZ',
'ONZE','DOZE','TREZE','QUARTOZE','QUINZE',
'DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
titulo = ' NÚMERO POR EXTENSO '

while True:
    n = int(input('Digite um número entre 0 a 20: '))
    while n < 0 or n > 20:
        n = int(input('Valor inválido!Digite um número entre 0 a 20: '))
    print('='*30)
    print(f'{titulo:-^30}')
    print('='*30)
    print(f'NÚMERO SOLICITADO: {n}.'
          f'\nNÚMERO POR EXTENSO: {numeros[n]}.')
    sair = str(input('Deseja visualizar mais algum número[S/N]: ')).strip().upper()
    while sair!= 'N' and sair!= 'S':
        sair = str(input('Valor inválido! Deseja realmente visualizar mais algum número[S/N]: ')).strip().upper()
    if sair == 'N':
        break

print('\nPROGRAMA FINALIZADO PELO USUÁRIO!!!')