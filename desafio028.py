"""Escreva um programa que faça o computador pensar em um número inteiro
entre 1 e 5 e pça para o usuário tentar descobrir qual foi o o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou não."""

import random
print('Olá, nesse jogo, você que adivinhar o número escolhido pelo computador. Este número está entre 1 e 5! Boa sorte!')
n = int(input('digite um número entre 1 e 5: '))
if n > 5:
    print('Você escolheu um número errado, por favor tente novamente.')
elif n < 1:
    print('Este número não está entre os números possíveis, por favor, tente novamente.')
else:
    pc = [1, 2, 3, 4, 5]
    pcchoice = random.choice(pc)
    """print(n)
    print(pcchoice)"""
    if n == pcchoice:
        print('Parabéns você acertou o número escolhido pelo computador que é o número {}'.format(pcchoice))
    else:
        print('Que pena, você errou! O Número escolhido pelo computador foi o {}'.format(pcchoice))
print('Obrigado por jogar!')