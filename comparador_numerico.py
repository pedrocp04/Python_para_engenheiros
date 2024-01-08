entrada = input('Digite um número: ')

try:
    x = int(entrada)
    if x > 0:
        print('Número positivo')
    elif x < 0:
        print('Número negativo')
    else:
        print('Zero')
except ValueError:
    print('Não é um número inteiro')

