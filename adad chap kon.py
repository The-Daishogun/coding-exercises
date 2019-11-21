string = input()
for i in range(0, len(string)):
    num = int(string[i])

    if num != 0:
        pwr = 1
        for p in range(0, num-1):
            pwr = (pwr*10)+1
        output = num * pwr
        print(string[i] + ":", output)
    else:
        print(string[i] + ":")

