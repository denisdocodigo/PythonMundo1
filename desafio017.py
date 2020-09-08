#Faça um programa que leia o comprimento do cateto oposto e adjacente
#de um triângulo, calcule e mostre o comprimento de sua hipotenusa.

from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(catad, catop)

print('O valor do comprimento da hipotenusa é {}'.format(hip))