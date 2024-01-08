lista_num_primos = [2]

prox_elemento = 2

while len(lista_num_primos) < 50:
    prox_elemento += 1
    prox_elemento_status = ""

    for elemento in lista_num_primos:
        quociente = prox_elemento/elemento
        quociente_int = prox_elemento // elemento

        if  quociente_int == quociente:
            prox_elemento_status = "pula"
            break
    
    if prox_elemento_status == "pula":
        continue
    else:
        lista_num_primos.append(prox_elemento)

print(lista_num_primos)
