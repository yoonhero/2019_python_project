usernames = []
numbers = []
answer = input("what do you want(login or creat): ")
if answer == "Login" or "login":
    login()

elif answer == "creat" or "Creat":
    creat()
else:
    print("write again")

def creat():
    username = input("name: ")
    usernames.append(username)
    number = input("number: ")
    numbers.append(number)
    return

def login():
    a = input("what your ID: ")
    if a in usernames:
        i = 0
        for i in range(usernames[i] == a):
            i += 1

    else:
        print("no user")

    ab = i
    b = input("what your PIN: ")

    if a in numbers:
        i = 0
        for i in range(usernames[i] == b):
            i += 1

    abc = int(i)

    if ab == abc:
        print("hello world")

    else:
        print("try again")

    return print("hello")



