num = 1
i = 0
result = 0
j = 0
primefactor = []
while i <= num:
    i += 1
    if num % i == 0:
        result = i
        j = 0
        primefactor.clear()
        while j <= result:
            j += 1
            if result % j == 0:
                primefactor.append(j)
        if len(primefactor) == 2:
            print(result)