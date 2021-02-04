num = 5
result = num
plu = 0
pu = 0
count = 0
le = 0
for i in range(1, num - 1):
    le += 1

for j in range(1, num):
    plu += j


while True:
    if plu >= num:
        pus= plu
        result += pus
        count += 1
    for x in range(2, num):
        if le - count >= x:
            pus = pus * 2
            result += pus
            count += 1
    if le - count == 1:
        result = result * 2
        count += 1
        if count == le:
            print(result)
            break