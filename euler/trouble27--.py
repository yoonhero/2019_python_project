num = 39
j = 0
li = []
count = 0
result = 0
for j in range(0, num + 1):
    li.clear()
    result = j ** 2 + j + 41
    for i in range(1, result + 1):
        if result % i == 0:
            li.append(i)
    if len(li) == 2:
        count += 1
print(count)

for j in range(0, num + 1):
    li.clear()
    result = j ** 2 + j + 41
    for i in range(1, result + 1):
        if result % i == 0:
            li.append(i)
    if len(li) == 2:
        count += 1
