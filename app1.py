def unlock():
    global a
    if password == "abcd":
        a = 1
    print("Evaluating password")
    while a < 4:
        print(str(a) + "...")
        a += 1
    print("Access Granted")


username = input("What is the username?: ")
if username == "Colin":
    password = input("Welcome Colin what is your password?: ")
    unlock()
