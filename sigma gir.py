from _decimal import Decimal


def calculate(n, m):
    output = 0
    for i in range(-10, m + 1):

        loop_result = 0

        for j in range(1, n + 1):
            result = (i + j) ** 3
            result = Decimal(result) // Decimal(j ** 2)

            loop_result += result

        output += loop_result
    return output


n = int(input())
m = int(input())

print(calculate(n,m))
