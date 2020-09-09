"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

ano = int(input('Digite o ano e te mostro se ele é bissexto: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano de {} é bissexto'.format(ano))
        else:
            print('O ano de {} não é bissexto'.format(ano))
    else:
        print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))