"""Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome"""
nome = input('Digite seu nome: ').strip()
snome = nome.split()
print('Seu nome possui Silva? ')
print('Silva' in snome)