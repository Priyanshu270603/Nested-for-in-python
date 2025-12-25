balance = 1000

while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Please enter your choice: "))

        if choice == 1:
            print("Current Balance:", balance)

        elif choice == 2:
            deposit = int(input("Enter the amount you want to deposit: "))
            balance += deposit
            print("Current Balance:", balance)

        elif choice == 3:
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw > balance:
                print("Insufficient funds")
            else:
                balance -= withdraw
                print("Withdrawal Successful!")

        elif choice == 4:
            print("Transaction Complete, Thank You!.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter numeric values only.")
