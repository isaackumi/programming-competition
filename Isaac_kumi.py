def Sum_of_triangular_numbers(n):
    if n < 0:
        return 0
    my_sum = 0
    
    for i in range(n+1):
        my_sum+= i
    return my_sum + (n * (n + 1)) // 2

    
