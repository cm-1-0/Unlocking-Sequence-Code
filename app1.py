prompt = input("Would you like to access this program?: ")
while prompt == "Yes":
    text = input("Would you like to access your account: ")
    if text == "Yes":
        username = input("Enter your username: ")
        if username == "Colin":
            password = input("Welcome Colin what is your password?: ")
            if password == "abcd":
                a = 1
                print("Evaluating password")
                while a < 4:
                    print(str(a) + "...")
                    a += 1
                print("Access Granted")
            else:
                print("Try again")
        else:
            print("Enter a valid username")
        break
if prompt == "No":
    print("Thank You and come again")




