def prime_checker(a, b):
    array = []
    for num in range(a+1, b):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                array.append(num)
    return array


a = int(input())
b = int(input())

array = prime_checker(a, b)
output=""
for i in range(len(array)):
    output += str(array[i])
    if i < len(array) - 1:
        output += ","
print(output)
