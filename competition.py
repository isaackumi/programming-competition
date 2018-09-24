def triangular(n):
    sum_ = 0
    total=0
    for i in range(n+1):
        for j in range(n):
            sum_+= i
            total+=j
        print(total)
    return sum_ 
