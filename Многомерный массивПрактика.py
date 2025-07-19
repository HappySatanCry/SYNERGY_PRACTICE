def min_max_array(arr_A):
    min_index = arr_A.index(min(arr_A)) 
    max_index = arr_A.index(max(arr_A)) 
    
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    
    save_sum = 0
    for i in range (start, end):
        if arr_A [i] < 0:
            save_sum += arr_A [i]
            
    return save_sum

result = min_max_array([3, 2, 0, -2, 2, -9, 2])

print(result)
            




