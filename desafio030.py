"""Crie um programa que leia o número inteiro e mostre na tela
se ele é par ou impar."""

n = int(input('Digite um número inteiro qualquer: '))
if n % 2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O númeor é impar')
