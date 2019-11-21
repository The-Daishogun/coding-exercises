def ladderGCD(m, n):

    m = abs(m)
    n = abs(n)

    if m == 0:
        return n
    elif n == 0:
        return m

    if n > m:
        if n % m == 0:
            return m
        else:
            return ladderGCD(n % m, m)
    else:
        if m % n == 0:
            return n
        else:
            return ladderGCD(n, m % n)


a = int(input())
b = int(input())

print(ladderGCD(a, b))


