password = input("Enter your password: ")
has_uppercase = False

for char in password:
    if char.isupper():
        has_uppercase = True
        break 

if len(password) < 8:
    print("Password is too short.")
elif not has_uppercase:
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")

