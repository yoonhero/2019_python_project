count = {}
import math
def result(i, hello, count):
    result = 1 / i
    result = '%.5000f' % result
    result = str(result[2:])
    for j in range(0, len(result)):
        for x in range(0, j):
            if result[x:j] == result[j:2*j-x] == result[2*j-x:3*j-2*x]:
                num = j - x
                real = 4998 - x
                he = j - x
                if result[x:] == "0" * real:
                    break
                elif result[x:j] == result[j:2 * j - x] == "0" * he:
                    continue
                else:
                    count[j - x] = i
                    hello = False
        if hello == False:
            break
for i in range(2, 1001):
    result(i, True, count)

print(count)
