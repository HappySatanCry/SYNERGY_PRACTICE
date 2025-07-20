def sum_negative_arr_A(arr):
    if len(arr) <= 2: 
        return 0
    
    sorted_arr = sorted(arr) 
    sum_neg = 0

    for num in sorted_arr[1:-1]:
        if num < 0:
            sum_neg += num

    return sum_neg

print(sum_negative_arr_A([2, -4, -9, 4, 1, -2, 7, -4]))