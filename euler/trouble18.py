num = 100
result = 1
real = 0
for i in range(1, num + 1):
    result = result * i
result = str(result)
for j in range(0, len(result)):
    real += int(result[j])
print(real)