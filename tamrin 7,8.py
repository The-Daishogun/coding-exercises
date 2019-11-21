#tamrin 7:


def test(argument):
    print(argument)


def reverse(string):
    return string[::-1]


def mirror(string):
    mirrored = reverse(string)
    return string+mirrored


print("Tamrin 7:")
test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")
print()

#tamrin 8:

print("Tamrin 8:")
test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")