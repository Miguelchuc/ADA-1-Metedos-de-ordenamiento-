def insertion_sort(arr, key):
    o
    for i in range(1, len(arr)):
       
        current_dict = arr[i]
       
        j = i - 1
        while j >= 0 and arr[j][key] > current_dict[key]:  
            arr[j + 1] = arr[j]  
            j -= 1
        
      
        arr[j + 1] = current_dict
        
  
        print(f"Iteración {i}: {arr}")
    
    return arr

personas = [
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Marta", "edad": 27},
    {"nombre": "Pedro", "edad": 19}
]

print("Lista original:", personas)
personas_ordenadas = insertion_sort(personas, "edad")
print("Lista ordenada por edad:", personas_ordenadas)

