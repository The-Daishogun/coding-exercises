def adder(args):
    total = "0"
    for arg in args:
        total = str(int(total) + int(arg))
    return total


n = int(input())
array = []
for i in range(n):
    array.append(input())

print(adder(array))
