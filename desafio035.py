"""Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem fazer um triângulo ou não.

-Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas
dos outros dois e maior que o valor absoluto da diferença entre essas medidas."""

a = int(input('Digite o valor para o lado A do triangulo: '))
b = int(input('Digite o valor para o lado B do triangulo: '))
c = int(input('Digite o valor para o lado C do triangulo: '))

if (a < (b+c)) and (b < (a+c)) and (c < (a+b)):
    print('É um triângulo.')
else:
    print('Não é triângulo.')


