def password_strength_checker(password):
    length = len(password)

    upper = 0
    lower = 0
    digit = 0
    special = 0

    for ch in password:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
             lower = lower + 1
        elif ch.isdigit():
             digit = digit + 1
        else:
            special = special + 1

    if length >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
        return "Strong Password ✅"
    elif length >= 6 and upper > 0 and lower > 0 and digit > 0:
        return "Medium Password ⚠️"
    else:
       return "Weak Password ❌"
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    print(password_strength_checker(password))