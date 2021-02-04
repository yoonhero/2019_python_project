li = []

def hi(a, li):
    for i in range(1, len(li)):
        if li[i] == a:
            continue
        else:
            append(a, li)

def append(a, li):
    li.append(a)
    print(li)

result = 0
for a in range(2, 6):
    for b in range(1, 10):
        result = a ** b
        hi(result, li)

print(len(li), li)
