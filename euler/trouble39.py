count = 0
con = {}
def ran(con, count):
    for a in range(1, num):
        for b in range(1, num):
            for c in range(1, num):
                if a + b + c == num and a + b > c and a <= b <= c:
                    count += 1
                    print(num, a, b, c)
                    if a == b == c:
                        break
    con[count] = num
for num in range(1, 1001):
    count = 0
    ran(con, count)

print(con)
print(con[max(con)])
