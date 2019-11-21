numList=[]

for i in range(0, 3):
    numList.append(int(input()))

numList.sort(reverse=True)
if numList[0]**2 == numList[1]**2 + numList[2]**2:
    print("YES")
else:
    print("NO")
