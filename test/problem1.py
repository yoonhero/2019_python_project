N = 1000000
count = 0
result = 0
for i in range(1, N + 1):
    try:
        result = 0
        length = int(len(str(i)))
        for j in range(0, length):
            num = str(i)
            num = int(num[j])
            result += num
        if i % result == 0:
            count += 1
    except ZeroDivisionError:
        print("")
print(count)