result = 0

def hello(result):
    if int(i[2]) == 1:
        result += 3
    elif int(i[2]) == 2:
        result += 3
    elif int(i[2]) == 3:
        result += 5
    elif int(i[2]) == 4:
        result += 4
    elif int(i[2]) == 5:
        result += 4
    elif int(i[2]) == 6:
        result += 3
    elif int(i[2]) == 7:
        result += 5
    elif int(i[2]) == 8:
        result += 5
    elif int(i[2]) == 9:
        result += 4

for i in range(1, 1001):
    i = str(i)
    if int(len(i)) == 1:
        if int(i) == 1:
            result += 3
        elif int(i) == 2:
            result += 3
        elif int(i) == 3:
            result += 5
        elif int(i) == 4:
            result += 4
        elif int(i) == 5:
            result += 4
        elif int(i) == 6:
            result += 3
        elif int(i) == 7:
            result += 5
        elif int(i) == 8:
            result += 5
        elif int(i) == 9:
            result += 4
    elif int(len(i)) == 2:
        if int(i[0]) == 1:
            if int(i) == 11:
                result += 6
            elif int(i) == 12:
                result += 6
            elif int(i) == 13:
                result += 8
            elif int(i) == 14:
                result += 8
            elif int(i) == 15:
                result += 7
            elif int(i) == 16:
                result += 7
            elif int(i) == 17:
                result += 9
            elif int(i) == 18:
                result += 9
            elif int(i) == 19:
                result += 8
            elif int(i) == 10:
                result += 3
        else:
            if int(i[0]) == 2:
                result += 6
            elif int(i[0]) == 3:
                result += 6
            elif int(i[0]) == 4:
                result += 5
            elif int(i[0]) == 5:
                result += 6
            elif int(i[0]) == 6:
                result += 5
            elif int(i[0]) == 7:
                result += 7
            elif int(i[0]) == 8:
                result += 7
            elif int(i[0]) == 9:
                result += 6
            if int(i[1]) == 1:
                result += 3
            elif int(i[1]) == 2:
                result += 3
            elif int(i[1]) == 3:
                result += 5
            elif int(i[1]) == 4:
                result += 4
            elif int(i[1]) == 5:
                result += 4
            elif int(i[1]) == 6:
                result += 3
            elif int(i[1]) == 7:
                result += 5
            elif int(i[1]) == 8:
                result += 5
            elif int(i[1]) == 9:
                result += 4
    elif int(len(i)) == 3:
        if int(i[0]) == 1:
            result += 3 + 7
        elif int(i[0]) == 2:
            result += 3 + 7
        elif int(i[0]) == 3:
            result += 5 + 7
        elif int(i[0]) == 4:
            result += 4 + 7
        elif int(i[0]) == 5:
            result += 4 + 7
        elif int(i[0]) == 6:
            result += 3 + 7
        elif int(i[0]) == 7:
            result += 5 + 7
        elif int(i[0]) == 8:
            result += 5 + 7
        elif int(i[0]) == 9:
            result += 4 + 7
        if int(i[1]) == 1:
            if int(i[1:]) == 11:
                result += 6 + 3
            elif int(i[1:]) == 12:
                result += 6 + 3
            elif int(i[1:]) == 13:
                result += 8 + 3
            elif int(i[1:]) == 14:
                result += 8 + 3
            elif int(i[1:]) == 15:
                result += 7 + 3
            elif int(i[1:]) == 16:
                result += 7 + 3
            elif int(i[1:]) == 17:
                result += 9 + 3
            elif int(i[1:]) == 18:
                result += 9 + 3
            elif int(i[1:]) == 19:
                result += 8 + 3
            elif int(i[1:]) == 10:
                result += 3 + 3
        else:
            if int(i[1]) == 2:
                result += 6 + 3
                hello(result)
            elif int(i[1]) == 3:
                result += 6 + 3
                hello(result)
            elif int(i[1]) == 4:
                result += 5 + 3
                hello(result)
            elif int(i[1]) == 5:
                result += 6 + 3
                hello(result)
            elif int(i[1]) == 6:
                result += 5 + 3
                hello(result)
            elif int(i[1]) == 7:
                result += 7 + 3
                hello(result)
            elif int(i[1]) == 9:
                result += 6 + 3
                hello(result)
            elif int(i[1]) == 0:
                if int(i[2]) == 1:
                    result += 3 + 3
                elif int(i[2]) == 2:
                    result += 3 + 3
                elif int(i[2]) == 3:
                    result += 5 + 3
                elif int(i[2]) == 4:
                    result += 4 + 3
                elif int(i[2]) == 5:
                    result += 4 + 3
                elif int(i[2]) == 6:
                    result += 3 + 3
                elif int(i[2]) == 7:
                    result += 5 + 3
                elif int(i[2]) == 8:
                    result += 5 + 3
                elif int(i[2]) == 9:
                    result += 4 + 3
    elif int(len(i)) == 4:
        result += 3 + 8

print(result)

