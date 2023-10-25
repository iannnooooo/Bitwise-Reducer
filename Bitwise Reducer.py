def solution(n):
    n = int(n)
    
    counter = 0
    while n > 3:
        if n & 1:
            if n & 2:
                n = (n + 1) >> 2
                counter += 3
            else:
                n = (n - 1) >> 1
                counter += 2
        else:
            n = n >> 1
            counter += 1
    
    if n == 3:
        n = n - 1
        counter += 1

    if n == 2:
        n = n - 1
        counter += 1

    return counter