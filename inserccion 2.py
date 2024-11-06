def insertion_sort(arr):
   
    for i in range(1, len(arr)):
        
        current_tuple = arr[i]
        
      
        j = i - 1
        while j >= 0 and arr[j][1] > current_tuple[1]:  
            arr[j + 1] = arr[j] 
            j -= 1
        
     
        arr[j + 1] = current_tuple
        
      
        print(f"Iteración {i}: {arr}")
    
    return arr


tuplas = [("Carlos", 25), ("Ana", 30), ("Luis", 22), ("Marta", 27), ("Pedro", 19)]
print("Lista original:", tuplas)
tuplas_ordenadas = insertion_sort(tuplas)
print("Lista ordenada por el segundo valor:", tuplas_ordenadas)


