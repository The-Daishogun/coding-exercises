def fibonacci_gen(n):
    a = 1
    b = 1
    for i in range(n):
        yield a + b
        temp = a
        a += b
        b = temp


a = fibonacci_gen(int(input("How many fibonacci numbers do you want??\n")))
for item in a:
    print(item)
