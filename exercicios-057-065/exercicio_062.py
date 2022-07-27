# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
titulo = 'VÁRIOS TERMOS DE UMA PA'
print('='*40)
print(f'{titulo:-^40}')
print('='*40)
termo1 = int(input('O PRIMEIRO TERMO DA PA DESEJADA: '))
r = int(input('A RAZÃO DESSA PA: '))
c = soma_termos = 0
cont = termos = 10
print(f'OS 10 PRIMEIROS TERMOS DESSA PA SÃO: ',end=' ')
while termos !=0:
    if cont == termos:
        while c < termos:
            if c < termos:
                soma_termos += r
                print(termo1,end=' -> ')

            else:
                print(termo1,end='')
            c += 1
            cont-=1
            termo1 += r
    print('PAUSA')
    cont=0
    c = 0

    termos = int(input('\nDESEJA VIZUALIZAR + TERMOS DESSA PA?'
                       '\nSE SIM DIGITE QUANTOS, SENÃO DIGITE 0: '))
    if termos !=0:
        print(f'O(S) PRÓXIMO(S) {termos} TERMO(S) DESSA PA É/SÃO:',end=' ')
        if cont == 0:
            while c < termos:
                if c < termos:
                    soma_termos += r
                    print(termo1,end=' -> ')

                else:
                    print(termo1,end='')
                c += 1
                cont-=1
                termo1 += r

        cont=0
        c = 0
    else:

        print('\nPROGRAMA ENCERRADO PELO USUÁRIO!\nOBRIGADO POR UTILIZAR NOSSO GERADOR DE PA!')






