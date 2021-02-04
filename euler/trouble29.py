Re = []
count = 0

for a in range(2, 101):
    for b in range(2, 101):
        result = a ** b
        if result not in Re:
            Re.append(result)
            count += 1
print(count)

def append(result, count):
    Re.append(result)
    count += 1


def hel(Re, result, count):
    if result not in Re:
        append(result, count)


def ran(start, end, Re):
    for i in range(start, end):
        for x in range(start, end):
            result = i ** x
            hel(Re, result, count)
    print(count)


print(ran(2, 101, Re))
