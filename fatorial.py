n = int(input('Digite um número: '))

fat = 1

if type(n) is int:
    while n> 0:
        fat *= n
        n -= 1

fat
