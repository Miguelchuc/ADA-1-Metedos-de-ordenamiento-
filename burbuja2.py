def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Iteración {i+1}: {arr}")  
        for j in range(0, n-i-1):
            print(f"  Comparando '{arr[j]}' con '{arr[j+1]}'")
            if len(arr[j]) > len(arr[j+1]):  
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"    Intercambiado: {arr}") 
        if not swapped:
            print(f"  No se realizaron intercambios, el arreglo está ordenado.")
            break
    return arr


cadenas = ["manzana", "kiwi", "banana", "cereza", "uva", "pera"]
print("Lista original:", cadenas)
cadenas_ordenadas = bubble_sort(cadenas)
print("Lista ordenada por longitud:", cadenas_ordenadas)


