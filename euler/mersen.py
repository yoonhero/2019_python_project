list = [2]
mersen = []
count = 0 
for i in range(1, 1000):
	mersen.append(2**i -1)
def prime(count):
	#input_num = int(input("what num: "))
	input_num = 10000000000000000
	for i in range(2, input_num + 1):
		length = len(list)
		condition = True
		for j in range(0, length):
			if i % list[j] == 0:
				condition = False
				break
		if condition:
			if i in mersen:
				list.append(i)
				count += 1
				print(count, "th: " ,i)
prime(count)


