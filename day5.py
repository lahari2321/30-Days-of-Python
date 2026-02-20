def check_password_strength(password):
    upper=0
    lower=0
    digit=0
    special=0
    for char in password:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
        elif char.isdigit():
            digit+=1
        elif char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/":
            special+=1

    if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
            return "Strong password"
    elif len(password) >= 6 and (upper > 0 or lower > 0) and digit > 0:
            return "Moderate password"
    else:
            return "Weak password"
if __name__ == "__main__":
    print("Check the Strength of the password!----")
    password=input("Enter a password:--")
    print(check_password_strength(password))