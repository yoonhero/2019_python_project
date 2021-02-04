import math
hel = []
def fas(i, count, x):
    while i < 300000000:
        clean()
        i += 1
        x += i
        fa(x, 0, i)

def fa(x, j, i):
    while j <= x:
        j += 1
        if x % j == 0:
            append(j, x)

def append(j, x):
    hel.append(j)
    print(x, j, len(hel))
    if len(hel) >= 500:
        return print(x, "hello")

def clean():
    hel.clear()
print(fas(0, 0, 0))