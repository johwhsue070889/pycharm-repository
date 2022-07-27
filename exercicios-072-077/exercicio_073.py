# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Corinthias','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo',
'Vasco','Chapecoense','Atletico MG','Bota fogo','Atletico PR',
'Bahia','São Paulo','Fluminense','Sport','Vitoria',
'Coritiba','Avaí','Ponte preta','Atletico Go')
titulo = ' CAMPEONATO BRASILEIRO 2017 '
print('='*90)
print(f'{titulo:-^90}')
print('='*90)
print('a) Os 5 primeiros times de 2017 foram: ',end='')
cont=0
for c in range(0,5):
    if cont < 4:
        print(times[c],end=', ')
    else:
        print(times[c], end='.')
    cont+=1
print('\nb) Os últimos 4 colocados foram: ',end='')
for pos,c in enumerate (times):
    if pos >= 16 and pos <=18:
        print(c,end=', ')
    elif pos > 18:
        print(c, end='.')
print('\nc) Times em ordem alfabética:')
nova_ordem = sorted(times)
for c in range(0,20):
 print(nova_ordem[c])

print('d) Em que posição está o time da Chapecoense: ',end='')
for pos,c in enumerate (times):
    if c == 'Chapecoense':
        print(f'Ficou na {pos+1}° posição da tabela de 2017.')

