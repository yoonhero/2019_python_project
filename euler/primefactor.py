i = 0
j = 0
result = 0
li = []
attempt = 0

while True:
    if attempt == 10:
        print("51 merhan primefacotor founded" + result)
    i += 1
    result = 2 ** i - 1
    print(result)
    while j < result:
        j += 1
        if result & j == 0:
            li.append(j)
    if len(li) == 2:
        print(result + "and" + attempt)
        attempt += 1
        break
