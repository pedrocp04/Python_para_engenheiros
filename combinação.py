lista_de_letras = ['A', 'R', 'A', 'R', 'A']
lista_de_palavras = []
iteracoes = 0

for i5, L5 in enumerate(lista_de_letras):
    Lista_L5 = lista_de_letras.copy()
    Lista_L5.pop(i5)

    for i4, L4 in enumerate(Lista_L5):
        Lista_L4 = Lista_L5.copy()
        Lista_L4.pop(i4)

        for i3, L3 in enumerate(Lista_L4):
            Lista_L3 = Lista_L4.copy()
            Lista_L3.pop(i3)

            for i2, L2 in enumerate(Lista_L3):
                Lista_L2 = Lista_L3.copy()
                Lista_L2.pop(i2)

                for i1, L1 in enumerate(Lista_L2):
                    palavra = L5 + L4 + L3 + L2 + L1
                    iteracoes += 1

                    if palavra not in lista_de_palavras:
                        lista_de_palavras.append(palavra)

print(iteracoes)
print(lista_de_palavras)
