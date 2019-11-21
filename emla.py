def check_molana_or_hafez(string):
    if "MOLANA" in string or "HAFEZ" in string:
        return True
    else:
        return False


lst = []
output = ""
for i in range(5):
    lst.append(input())

for item in range(len(lst)):
    if check_molana_or_hafez(lst[item]):
        output += str(item+1) + " "

if output == "":
    output = "NOT FOUND!"
else:
    output = output.rstrip()


print(output)
