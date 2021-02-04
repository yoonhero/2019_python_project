i  = 0
result = 0
firesult = 0
for i in range(1, 101):
    result += i * i
    firesult += i
firesult = firesult * firesult
print(firesult - result)

