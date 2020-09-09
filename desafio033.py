"""Faça um programa que leia três números e mostre qual é o maior e o menor."""

n1 = int(input('Digite o valor de A: '))
n2 = int(input('Digite o valor de B: '))
n3 = int(input('Digite o valor de C: '))

if n3 < n1 > n2:
    if n3 > n2:
        print('O maior valor é A = {}\nO segundo maior valor é C = {}\nO terceiro maior valor é o B = {}'.format(n1,n3,n2))
    elif n3 == n2:
        print('O maior valor é A = {} e B e C tem o mesmo valor'.format(n1))
    else:
        print('O maior valor é A = {}\nO segundo maior valor é B = {}\nO terceiro maior valor é o C = {}'.format(n1,n2,n3))

elif n1 < n3 > n2:
    if n2 > n1:
        print('O maior valor é C = {}\nO segundo maior valor é B = {}\nO terceiro maior valor é o A = {}'.format(n3,n2,n1))
    elif n2 == n1:
        print('O maior valor é C = {} e A e B tem o mesmo valor'.format(n3))
    else:
        print('O maior valor é C = {}\nO segundo maior valor é A = {}\nO terceiro maior valor é o B = {}'.format(n3,n1,n2))

elif n1 < n2 > n3:
    if n1 > n3:
        print('O maior valor é B = {}\nO segundo maior valor é A = {}\nO terceiro maior valor é o C = {}'.format(n2,n1,n3))
    elif n1 == n3:
        print('O maior valor é B = {} e A e C tem o mesmo valor'.format(n2))
    else:
        print('O maior valor é B = {}\nO segundo maior valor é C = {}\nO terceiro maior valor é o A = {}'.format(n2,n3,n1))

elif n1 == n2 == n3:
    print('Os valores de A,B e C são iguais com o valor de {}.'.format(n1))

elif n1 == n2:
    if n3 > n1:
        print('O maior valor é C = {} e A e B tem o menor valor de {}'.format(n1, n3))
    else:
        print('A e B tem o maior valor de {} e o menor valor é C = {}'.format(n1, n3))
elif n1 == n3:
    if n2 > n1:
        print('O maior valor é B = {} e A e C tem o menor valor de {}'.format(n2, n3))
    else:
        print('A e B tem o maior valor de {} e o menor valor é C = {}'.format(n1, n2))
elif n3 == n2:
    if n1 > n2:
        print('O maior valor é A = {} e B e C tem o menor valor de {}'.format(n1, n3))
    else:
        print('B e C tem o maior valor de {} e o menor valor é A = {}'.format(n3, n3))