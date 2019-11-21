n = int(input())
total = 1

for i in range(2, n):
    if n % i == 0:
        total = i + total

if total == n:
    print("YES")
else:
    print("NO")
