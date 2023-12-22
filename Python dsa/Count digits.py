def count_digits(N):
    n = 0
    while N > 0:
        N //= 10
        n += 1
    return n

N = int(input("Enter Number: "))
result = count_digits(N)
print("Count of digits is:", result)


   
