import random
num = 2
x = 0
y = 0
count = 0
cou = 0
nu = []
nu1 = []
while cou <= num * 2:
    choice = random.randint(1, 2)
    if choice == 1:
        x += 1
        cou += 1
        nu.append(1)
        print("x", x)
        print(nu)
    elif choice == 2:
        cou += 1
        y += 1
        print("y", y)
        nu.append(2)
        print(nu)
    if cou == num * 2:
        if x == num & y == num:
            x = 0
            y = 0
            count += 1
            break
        else:
            x = 0
            y = 0
            count += 1

            break
print(count)
nu1 = nu
for q in range(1, len(nu)):
    nu.sort()
    num1 = len(nu) - 1
    num1 = int(num1 / 2)
    print(num1)
    if nu[num1] == nu[num1 + 1]:
        print("fail")
    else:
        print("success")
print(nu, nu1)


for xx in range(1, 3):
    for yy in range(1, 3):