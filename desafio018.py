#faça um programa que leia um ângulo qualquer e mostre na tela
#o valor de seno, cosseno e tangente desse ângulo.

import math
a = float(input('Digite o valor em graus do ângulo: '))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O ângulo {}, tem como valor de seno: {:.2f}\nCosseno {:.2f}\nTangente {:.2f}'.format(a, sin, cos, tan))