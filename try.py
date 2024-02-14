def collatz(n):
    # inc = 1
    c = []
    c.append(n)
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        
        else:
            n = 3 * n + 1
            
        print(c.append(n))
        
    return c


j = int(input("Enter a number greater than zero> "))
result = collatz(j)
print(result)