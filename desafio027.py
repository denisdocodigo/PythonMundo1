"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente."""

nome = str(input('Digite seu nome completo: ')).strip()
snome = nome.split()
lastname = len(snome) - 1
print('Olá, {} {}! Seja bem vindo!'.format(snome[0].capitalize(), snome[lastname].capitalize()))