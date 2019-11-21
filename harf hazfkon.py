def remove_letter(letter, string):
    string = list(string)
    for char in string:
        if char == letter:
            string.remove(letter)
            return remove_letter(letter, string)
    return "".join(string)

a = input().split()
letter_to_remove = a[0]
string_to_check = a[1]

print(remove_letter(letter_to_remove, string_to_check))