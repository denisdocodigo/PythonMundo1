"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados"""
n = int(input('Digite um número de 0 a 9999: '))
n2 = n + 10000
n2 = str(n2)
print('O numero escolhido foi {}\n'.format(n))
print('Unidade: {}:'.format(n2[4]))
print('Dezena: {}'.format(n2[3]))
print('Centena: {}'.format(n2[2]))
print('Milhar: {}'.format(n2[1]))