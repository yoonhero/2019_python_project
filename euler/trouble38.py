result = ""

for i in range(1, 10000):
    result = ""
    for j in range(1, 100):
        result += str(i * j)
        if len(result) == 9:
            if not "0" in result:
                if "1" in result and "2" in result and "3" in result and "4" in result and "5" in result and "6" in result and "7" in result and "8" in result and "9" in result:
                    print(result, i, "hello")

