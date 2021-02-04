list = [2]
def prime(num):
	#input_num = int(input("what num: "))
	input_num = 10000
	for i in range(2, input_num + 1):
		length = len(list)
		condition = True
		for j in range(0, length):
			if i % list[j] == 0:
				condition = False
				break
		if condition:
			print(i)
			list.append(i)
	return list
list = prime(list)
mersen = []
for i in range(1, 1000):
	mersen.append(2**i -1)

for i in range(0, len(mersen) - 1):
	if mersen[i] in list:
		print("mersen: ", mersen[i])











