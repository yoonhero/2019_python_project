i = 0
j = 0
sequence = []
maxnum = 0
lennum = [0]
while i < 1000000:
    i += 1
    j = i
    sequence.append(j)
    while True:
        if j % 2 == 0:
            j = j / 2
            sequence.append(j)
            if j == 1:
                break
        else:
            j = 3 * j + 1
            sequence.append(j)
    if len(sequence) > max(lennum):
        lennum.clear()
        lennum.append(len(sequence))
        maxnum = i
    sequence.clear()
print(maxnum)