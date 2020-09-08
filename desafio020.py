#O mesmo professor do exercício anterior que sortear a ordem de
#apresentação dos trabalhos dos alunos. Faça um programa que leia
#o nome dos quatro alunos e mostre a ordem sorteada.

import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Difite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
escolhido = random.shuffle(lista)

print(lista)