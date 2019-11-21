def reverse(string):
    return string[::-1]


def mirror(string):
    mirrored = reverse(string)
    return string+mirrored


string = input()

print(mirror(string))
