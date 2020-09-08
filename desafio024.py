"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com SANTO"""
nome = input('Digite o nome de sua cidade: ').strip()
print('Sua cidade começa com o nome Santo? ')
pnome = nome.split()
print('Santo' in pnome[0])