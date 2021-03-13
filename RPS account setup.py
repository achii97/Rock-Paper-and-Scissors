print("-----------------------------------")
print("Rock, Paper, Scissors Account Setup")
print("-----------------------------------")

while True:
    username = input("Enter a username = ")
    password = input("Enter a password = ")
    password_confirm = input("Confirm password = ")

    if password != password_confirm:
        print("Your Password do not match!")

    if password == password_confirm:
        print("Your Account has been setup.")
        text_file = open("accounts.txt","a")
        #text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close() 
        break
