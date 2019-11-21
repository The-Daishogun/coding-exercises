def add_it_all_up(num):
    num = str(num)
    total = 0
    for digit in num:
        total += int(digit)
    if total < 10 :
        return total
    else:
        return add_it_all_up(total)


a = add_it_all_up(int(input()))
print(a)