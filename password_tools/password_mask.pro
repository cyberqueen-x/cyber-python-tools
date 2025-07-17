import getpass
attempts = 3
while attempts > 0:
    password = getpass.getpass("Enter you passwrod: ")
    confirm_password = getpass.getpass("confirm your password: ")
    if password == confirm_password:
        print("✅ your password set successfully!")
        break
    else:
        attempts -= 1
        print(f"your password is unmatched, attempts left {attempts}")
if attempts == 0:
    print("too many failed attempts, try again later")
                                                                                     
       
