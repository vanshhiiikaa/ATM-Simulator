print("Welcome to ATM Simulator")
pin = int(input("Enter your PIN: "))

accounts ={
    1234 : {
        "Name" : "Rahul" ,
        "PIN" : 1234,
        "Balance" : 10000 ,
        "Transactions" : []
    } ,
    5678 : {
        "Name" : "Lily" ,
        "PIN" : 5678 ,
        "Balance" : 2000,
        "Transactions" : []
    }
}


if pin in accounts:
    print("PIN Exists")
    print("Welcome ",accounts[pin]["Name"])

while True:
    feature = int(input("Enter keys for selected options\n1 for check balance\n2 for depostis\n3 for withdraws\n4 to change PIN\n5 for mini statement\n6 to EXIT\n>"))

    if feature == 1:
        print("Your Remaining balance is : Rs.",accounts[pin]["Balance"])

    elif feature == 2:
        deposit = int(input("Enter the amount you want to deposit: "))

        if deposit > 0:
            accounts[pin]["Balance"] += deposit
            accounts[pin]["Transactions"].append(f"Deposited Rs. {deposit}")
            print("Your total balance is", accounts[pin]["Balance"])

        else:
            print("Invalid deposit amount")

    elif feature == 3:
        withdraw = int(input("Enter the amount you want to withdraw: "))

        if withdraw > 0 and withdraw < accounts[pin]["Balance"]:
            accounts[pin]["Balance"] -= withdraw
            accounts[pin]["Transactions"].append(f"Withdraw Rs. {withdraw}")
            print("Remaining balance is : Rs.",accounts[pin]["Balance"])

        else:
            print("Invalid amount or insufficient balance")
    
    elif feature == 4:
        new_pin = int(input("Enter new PIN: "))

        if len(str(new_pin)) == 4:
            accounts[pin]["PIN"] = new_pin
            print("PIN Changed successfully")

            accounts[new_pin] = accounts.pop(pin)

        else:
            print("PIN must be of four digits")

    elif feature == 5:
        print("\nMini Statement:")

        if len(accounts[pin]["Transactions"]) == 0:
            print("No transactions available")

        else:
            for transaction in accounts[pin]["Transactions"]:
                print(transaction)

    elif feature == 6:
        print("Thanks for using ATM Simulator")
        break
    else:
        print("Invalid option")

else :
    print("Invalid PIN")