pentagon_num = []
for i in range(1, 1000):
    pentagon_num.append(int(i * (3 * i - 1) / 2))
for j in range(0, 999):
    for x in range(0, 999):
        result1 = pentagon_num[j] - pentagon_num[x]
        result2 = pentagon_num[j] + pentagon_num[x]
        for a in range(1, 999):
            if result1 == pentagon_num[a]:
                for b in range(1, 999):
                    if result2 == pentagon_num[b]:
                        print(result1, result2)
print(pentagon_num)
