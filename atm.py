balance = int(input("Enter current balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount % 100 != 0:
    print("Withdrawal amount must be multiple of 100")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Please collect cash")
    print("Updated balance:", balance)