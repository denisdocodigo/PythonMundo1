#Escreva um programa que calcule a quantidade de km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele
#foi alugado. Calcule o preço a pagar, sabendo que o carro custa
#R$60 e R$0,15 por km rodado.

dias = int(input('Digite a quantidades de dias que o carro foi alguado: '))
km = float(input('Digite quantos KMs foram rodados: '))
t = dias*60 + (km*0.15)

print('O carro foi alugado por {} dias\nForam {}Kms rodados\nO total a ser pago é R${:.2f}'.format(dias, km, t))