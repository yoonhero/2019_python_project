firesult = []
result = 0
i = 20000
while i < 100000:
    i += 1
    j = 0
    firesult.clear()
    while j < i:
        j += 1
        if i % j == 0:
            firesult.append(j)
    if len(firesult) == 2:
        result += i
print(result + 21171191)