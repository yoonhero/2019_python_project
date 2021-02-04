mul1 = 3
mul2 = 5
num1 = 0
num2 = 0
result1 = 0
result2 = 0
result3 = 0
i = 0
y = 0
c = 0
lapping = 0
z = 0

while i < 10000000000000000000000000:
    i += 1

    num1 = mul1 * i
    if num1 >= 10000000:
        break
    else:
        result1 += num1

while y < 100000000000000000000000000:
    y += 1
    num2 = mul2 * y
    if num2 >= 10000000:
        break
    else:
        result2 += num2

while z < 1000000000000000000000000000:
    z += 1
    lapping = 15 * z
    if lapping >= 10000000:
        break
    else:
        result3 += lapping


def add(result1, result2, result3):
    c = result1 + result2 - result3
    return c

print(add(result1, result2, result3))
