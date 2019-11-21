import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset == set(str1)


first_line = input().split(" ")
n = int(first_line[0])
alefba = first_line[1]

codes = []

for i in range(0, n):
    code_to_test = input()
    codes.append(code_to_test)

for code in codes:
    code = list(code)

    if ispangram(code, alefba):
        print("Yes")
    else:
        print("No")
