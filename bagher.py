def check(string):
    if "HAFEZ" in string or "MOLANA" in string:
        return True
    else:
        return False


output = ""
for i in range(5):
    a = check(input())
    if a:
        output += str(i + 1) + " "

if output == "":
    output = "NOT FOUND!"
else:
    output = output.rstrip()

print(output)
