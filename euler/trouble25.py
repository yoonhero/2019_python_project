count = 1
i = 1
prepre = 0
j = 0
result = 1
while True:
    result = int(result)
    result = i + j
    j = i
    i = result
    count += 1
    result = str(result)
    if len(result) >= 1000:
        print(result, count)
        break
