"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando por R# 0,50 por Km para viagens
de até 200km e R$ 0,45 para viagens mais longas"""

print('Olá, seja bem vindo ao agente de viagens automatizado.')
km = float(input('Digite a quantidade de Km necessário para sua viagem: '))
print('Você escolheu uma viagem de {} km. Está correta?\n'.format(km))
c = int(input('\nDigite 1 para confirma ou qualquer outro número para sair: '))
if c == 1:
    if km <= 200:
        preço = km*0.50
        print('O valor da sua passagem é de R$ {}'.format(preço))
    else:
        preço = km*0.45
        print('O valor da sua passagem é de R$ {}'.format(preço))
else:
    print('\nTente novamente quando souber a quantidade necessária!')
print('\nObrigado por utilizar o nosso terminal! Volte sempre!')