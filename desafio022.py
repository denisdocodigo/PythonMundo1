"""Crie um programa que leia o nome completo de uma pessoa e imprima na tela  :

- o nome com todas as letras maiúsculas
- o nome com todas as letras minúsculas
- Quantidade de letras sem conseiderar os espaços
- Quantas letras tem o primeiro nome"""

nome = input('Digite seu nome completo: ')
print('Seu nome completo com letras maiúsculas: ')
print(nome.upper())
print('Seu nome completo com letras minúsuclas:')
print(nome.lower())
print('Quantidade de letras sem contar os espaços: ')
tam = len(nome) - nome.count(' ')
print(tam)
print('A quantidade de Letra que contém o seu primeiro nome: ')
pnome = nome.split()
print(len(pnome[0]))