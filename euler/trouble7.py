i = 0
j = 0
result = 0
firesult = []
tempt = 0
while i < 1000000000:
    i += 1
    firesult.clear()
    j = 0
    while j < i:
        j += 1
        if i % j == 0:
            firesult.append(j)
    if len(firesult) == 2:
        tempt += 1
        result = i
    if tempt == 100001:
        print(result)
        break
