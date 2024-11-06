def burbuja_cadenas(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        print(f"Iteración {i+1}: Lista actual: {lista}")
        for j in range(0, n-i-1):
            print(f"  Comparando {lista[j]} con {lista[j+1]}")
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
                print(f"  Intercambiando {lista[j+1]} con {lista[j]}: {lista}")
        if not intercambiado:
            print("  No hubo intercambios, lista ya ordenada. Terminando...")
            break
    return lista

nombres = ["Carlos", "Ana", "Maria", "José", "Pedro"]
print("Lista antes de ordenar:", nombres)
burbuja_cadenas(nombres)
print("Lista después de ordenar:", nombres)

