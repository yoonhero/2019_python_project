mersen = []
for i in range(2, 10000):
	mersen.append(2**i-1)
for i in range(0, len(mersen)-1):
	num = mersen[i]
	condition = True
	for j in range(2,num-1):
		if num % j == 0:
			condition = False
			break
	if condition:
		print(num)