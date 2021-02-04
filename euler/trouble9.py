import math
for i in range(1, 500):
    for y in range(1, 500):
        for x in range(1, 500):
            result = i * i + y * y
            result2 = x * x
            if result == result2:
                if i + y + x == 1000:
                    print(i * y * x, "success")
                    break


