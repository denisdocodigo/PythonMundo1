"""Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.

Para salários superiores a R$ 1250,00 calcule um aumneto de 10%.
Para salários inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Digite o salário do funcionário à receber o aumento: '))
if salario <= 1250:
    salario = salario*1.15
    print('O funcionário teve um aumento de 15% e seu salário passar a ser R$ {:.2f}'.format(salario))
else:
    salario = salario*1.10
    print('O funcionário teve um aumento de 10% e seu salário passar a ser R$ {:.2f}.'.format(salario))