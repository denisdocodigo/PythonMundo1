"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite."""

km = float(input('Digite a velocidade do carro: '))
if km > 80:
    multa = km - 80
    print('Você foi multado por excesso de velocidade e passou {} na via de 80km/h\nExcedeu a velocidade em {} km/h. Sua multa será no total de R$ {}'.format(km,multa,multa*7))
else:
    print('Você está dentro do limite de velocidade da via.')