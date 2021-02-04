import random
num1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
num2 = "abcdefghijklmnopqrstuvwxyz"
num3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num4 = "!@#$%^&*()_+-=~`"
result = ""
def choice(start, end, num):
    choice = random.randint(start, end)
    result += num[choice]
for i in range(0, 10):
    choice = random.randint(1, 4)
    if choice == 1:
        choice(0, 9, num1)
    elif choice == 2:
        choice(0, 25, num2)
    elif choice == 3:
        choice(0, 25, num3)
    elif choice == 4:
        choice(0, 15, num4)
print(result)
