import decimal


def addition(nums):
    total = 0
    for num in nums:
        total += num
    return total


n = int(input())
array = []

for i in range(0, n):
    num = float(input()) * 1000
    num = int(num)
    array.append(num)

array.sort(reverse=True)


maximum = '{0:.3f}'.format(decimal.Decimal(array[0] / 1000))
minimum = '{0:.3f}'.format(decimal.Decimal(array[n-1] / 1000))

avg = '{0:.3f}'.format(decimal.Decimal((addition(array) / n) / 1000))


print("Max:", maximum)
print("Min:", minimum)
print("Avg:", avg)
