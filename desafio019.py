#Um professor quer sorter um de seus quatro alunos para apagar o quadro faça
#um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random
alunoa = input('Digite o nome do primeiro aluno: ')
alunob = input('Digite o nome do segundo aluno: ')
alunoc = input('Digite o nome do terceiro aluno: ')
alunod = input('Digite o nome do quarto aluno: ')
lista = [alunoa, alunob, alunoc, alunod]
print('O aluno sorteado para apagar o quadro foi {}.'.format(random.choice(lista)))