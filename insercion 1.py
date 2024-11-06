def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]  
        j = i - 1
        
        print(f"Iteración {i}: Clave = {clave}, Lista antes de insertar: {lista}")  
    
        while j >= 0 and lista[j] > clave:
            print(f"  Moviendo {lista[j]} hacia la derecha porque es mayor que {clave}")  
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave  
        print(f"  Después de insertar la clave: {lista}\n") 
    
    return lista

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista antes de ordenar:", numeros)
insercion(numeros)
print("Lista después de ordenar:", numeros)

