def seleccion(lista):
    n = len(lista)
    for i in range(n):
       
        min_idx = i
        print(f"Iteración {i+1}: Lista actual: {lista}")  
        for j in range(i + 1, n):
            print(f"  Comparando {lista[j]} con {lista[min_idx]}")  
            if lista[j] < lista[min_idx]:
                min_idx = j
                print(f"  Nuevo mínimo encontrado: {lista[min_idx]} en índice {min_idx}")
       
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        print(f"  Después de intercambio: {lista}\n")  
    return lista

numeros = [64, 25, 12, 22, 11]
print("Lista antes de ordenar:", numeros)
seleccion(numeros)
print("Lista después de ordenar:", numeros)
