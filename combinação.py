lista_de_letras = ['A','R','A','R','A']

lista_de_palavras =[ ]

iteracoes = 0

for i5 in range(len(lista_de_letras)):
    L5 = lista_de_letras[i5]
    Lista_L5 = lista_de_letras.copy()
    Lista_L4 = Lista_L5.copy()
    Lista_L4.pop(i5)
    for i4 in range(len(Lista_L4)):
        L4 = Lista_L4[i4]
        Lista_L3 = Lista_L4.copy()
        Lista_L3.pop(i4)
        for i3 in range(len(Lista_L3)):
            L3 = Lista_L3[i3]
            Lista_L2 = Lista_L3.copy()
            Lista_L2.pop(i3)
            for i2 in range(len(Lista_L2)):
                L2 = Lista_L2[i2]
                Lista_L1 = Lista_L2.copy()
                Lista_L1.pop(i2)
                for i1 in range(len(Lista_L1)):
                    L1 = Lista_L1[i1]
                    palavra = L5 + L4 + L3 + L2 + L1
                    if palavra not in lista_de_palavras:
                        lista_de_palavras.append(palavra)
