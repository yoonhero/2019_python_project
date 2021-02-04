
num1 = 1
num2 = 2
result = 0
final_result = 2
i = 0
while i < 1000000000:
    i += 1
    num1 += num2
    if num1 >= 4000000:
        break
    else:
        result = num1
        num1 = num2
        num2 = result
        if result % 2 == 0:
            final_result += result

print(final_result)
