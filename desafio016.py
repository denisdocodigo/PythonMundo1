#Crie um programa que leia um número real qualquer e mostre sua parte inteira.

from math import trunc
n = float(input('Digite um número com virgula para que o programa mostre sua parte inteira: '))
print('A parte inteira do número é {}'.format(trunc(n)))