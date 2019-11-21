n = float(input())
counter = 1
tavan=0

while tavan < n:
    tavan = 2 ** counter
    counter += 1
print(tavan)