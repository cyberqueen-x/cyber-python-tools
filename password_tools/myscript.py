def is_strong(password):
    if len(password) >= 8 and ("@" in password or "#" in password or "$" in password):
       return True
    else:
       return False
print(is_strong("admin@432"))
print(is_strong("abc"))

