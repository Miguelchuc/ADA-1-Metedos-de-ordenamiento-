def selection_sort_dates(dates):
    n = len(dates)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
           
            date_i = tuple(map(int, dates[i].split('/')))
            date_j = tuple(map(int, dates[j].split('/')))
        
                min_idx = j
        
      
        dates[i], dates[min_idx] = dates[min_idx], dates[i]
        
    
        print(f"Iteración {i + 1}: {dates}")
    
    return dates
fechas = ["23/11/2023", "01/05/2022", "15/03/2022", "10/08/2021", "05/12/2024"]
print("Lista original:", fechas)
fechas_ordenadas = selection_sort_dates(fechas)
print("Lista ordenada por fecha:", fechas_ordenadas)
