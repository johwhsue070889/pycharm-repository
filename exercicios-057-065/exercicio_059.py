# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

titulo = 'SISTEMA DE OPERAÇÕES'
titulo2 = 'MENU DE OPÇÕES:'
titulo3 = 'RESULTADO FINAL:'
print("="*90)
print(f'{titulo:^90}')
print("="*90)
sair = 0
opc = 0

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
while sair !='N' and sair !='n':
    print(f'ELEMENTOS DIGITADOS - > {n1} e {n2} ')
    print(f'\n{titulo2}')
    opc = int(input(f'[ 1 ] SOMAR'
                    f'\n[ 2 ] MULTIPLICAR'
                    f'\n[ 3 ] MAIOR ENTRE'
                    f'\n[ 4 ] TROCAR NÚMEROS'
                    f'\n\nDIGITE A OPERAÇÃO QUE DESEJA REALIZAR: '))
    while opc!=1 and opc!=2 and opc!=3 and opc!=4:
        opc = int(input('Valor inválido! Digite uma das opções do menu: '))
    if opc == 1:
        print(f'\n{titulo3:^90}')
        print()
        print(f'OPERAÇÃO ESCOLHIDA: SOMA'
              f' ENTRE OS ELEMENTOS {n1} e {n2}.'
              f'\nRESULTADO: {n1} + {n2} = {n1+n2}')
    elif opc == 2:
        print(f'\n{titulo3:^90}')
        print()
        print(f'OPERAÇÃO ESCOLHIDA: MULTIPLICAÇÃO'
              f' ENTRE OS ELEMENTOS {n1} e {n2}.'
              f'\nRESULTADO: {n1} x {n2} = {n1*n2}')
    elif opc == 3:
        print(f'\n{titulo3:^90}')
        print()
        print(f'OPERAÇÃO ESCOLHIDA: MAIOR VALOR ENTRE'
              f' OS ELEMENTOS {n1} e {n2}.')
        print('RESULTADO: ')
        if n1 > n2:
            print(f'O valor {n1} é o maior valor entre {n1} e {n2}!')
        elif n2 > n1:
            print(f'O valor {n2} é o maior valor entre {n1} e {n2}!')
        else:
            print(f'Valores iguais!!! Não há maior entre {n1} e {n2}!')

    if opc == 1 or opc == 2 or opc == 3:
        sair = str(input('Deseja realizar nova operação? [S/N]: ')).strip()[0]
        print()
        while sair != 'N' and sair != 'n' and sair !='S' and sair != 's':
            sair =  str(input('Valor inválido! Para confirmar pressione [S/N]: ')).strip()[0]
        print()
    elif opc == 4:
        print(f'OPERAÇÃO ESCOLHIDA: NOVOS VALORES')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        sair = 's'
print('Operação finalizada pelo usuário!')