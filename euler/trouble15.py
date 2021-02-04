num = str(2 ** 1000)
print(num)
result = 0
result1 = 0
for i in range(0, len(num)):
    result1 = num[i]
    result += int(result1)

print(result)