x = int(input('Digite um número: '))

if type(x) is str:
    print('Não é número')
elif x > 0:
    print('Número positivo')
elif x < 0:
    print('Número negativo')
elif x == 0:
    print('zero')
