"""Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes a letra A
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez"""

frase = str(input('Digite a sua frase: ')).lower().strip()
l = str(input())
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a')))
print('Ela aparece a primeira vez na {} posição.'.format(frase.find('a')+1))
print('Ela aparece na ultima vez na {} posição.'.format(frase.rfind('a')+1))

"""frase = input("Digite um frase: ").strip().upper()
letra = input("Qual letra você procura? ").strip().upper()

print("A sua frase possui {} letras {}'s".format(frase.count(letra), letra))

print("A primeiro letra '{}' está na {}° posição".format(letra,frase.find(letra)))

print("A última letra '{}' está na {}° posição".format(letra, frase.rfind(letra)))"""
