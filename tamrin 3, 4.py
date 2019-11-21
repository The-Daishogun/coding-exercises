def count_letter(string, letter):
    fruit = string
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    return count


def count_letter2(string, letter):
    count = 0
    for i in range(len(string)):
        m = string.find(letter, i)
        if i == m:
            count += 1
    print(count)


print(count_letter("banana", "a"))
print(count_letter2("banana", "a"))
