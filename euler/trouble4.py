i = 0
j = 0
result = 0
firesult = []

for i in range(100, 1000):
    for j in range(100, 1000):
        result = i * j
        reverse_result = int(str(result)[::-1])
        if result == reverse_result:
            firesult.insert(result, reverse_result)

print(max(firesult))