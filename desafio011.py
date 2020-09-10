#Faça um programa que leia a largura e a altura de uma parede em metros,
#Calcule a sua área e a quantidade de tinta necessária para pintala, sabendo
#que cada litro de tinta pinta uma área de 2m².

h = float(input('Digite a altura da parede: '))
l = float(input('Difite a comprimento: '))
a = h*l
print('A área da parede é de {:.2f}m²'.format(a))
print('Para pintar a parede serão necessários {} litros de tinta'.format(a/2))