def home_menu():
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Please select an option (1-4): ")
    return choice

def run_atm():
    pin = input("Please enter your PIN: ")
    if pin == account['pin']:
        while True:
            choice = display_menu()
            if choice == '1':
                check_balance()
            elif choice == '2':
                deposit_money()
            elif choice == '3':
                withdraw_money()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Erreur. Veuillez rentrer à nouveau votre choix (1-4).")
    else:
        print("Erreur. Essayez à nouveau.")
