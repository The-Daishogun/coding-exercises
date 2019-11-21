def full_line(num):
    output=""
    for i in range(n):
        output += "*"
    return output

def other_line(num):
    output = "*"
    for i in range(n-2):
        output += " "
    output += "*"

    return output


n = int(input())

print(full_line(n))

for i in range(n-2):
    print(other_line(n))

print(full_line(n))
