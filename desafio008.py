#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#=======================================================

m = float(input('Digite o valor em metros a ser convertido: '))
print('Medida em metros: {}m\nO valor em centimetros é {:.2f}cm \nO valor em milimetros {}mm'.format(m, m*100, m*1000))