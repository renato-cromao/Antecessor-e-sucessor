titulo = ('DINAMAXXX')
print('~'*40)
print('{:^50}'.format(titulo))
print('~'*40)
n1 = int(input('Digite um número que iremos informar seu sucessor e antecessor: '))
print('')
print('''
O seu antecessor é {}.
O número escolhido foi {}.
O seu sucessor é {}.

Portanto, o {} vem antes de {} e o {} vem depois.
'''.format(n1-1, n1, n1+1, n1-1, n1, n1+1))