def count_upper_case(string_object):
    counter = 0
    for char in string:
        if char.isupper():
            counter += 1
    return counter

def count_lower_case(string_object):
    counter = 0
    for char in string:
        if char.islower():
            counter += 1
    return counter

string = input()

print("it has {0} uppercase letters.".format(count_upper_case(string)))
print("it has {0} lowercase letters.".format(count_lower_case(string)))