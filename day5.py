print("Welocme to atm machine")
Balance=10000

option=input("Choose an option:--\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit:---------")
print(f"yor choose option is {option}")
if option == "1":
        print(f"Your balance is: {Balance}")
elif option == "2":
        amount=int(input("Enter a amount:--"))
        Balance += amount
        print(f"Your balance is now: {Balance}")
elif option == "3":
        amount=int(input("Enter a amount:--"))
        if amount <= Balance:
            Balance -= amount
            print(f"Your balance is now: {Balance}")
        else:
            print("Insufficient balance for the withdrawal.")
else:
        print("Exiting the program.")
