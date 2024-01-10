f = input("Digite um número: ")

try:
    f = int(f)
    fat = 1

    while f > 0:
        fat *= f
        f -= 1

    print("O fatorial é:", fat)

except ValueError:
    print('Não é um número!')
