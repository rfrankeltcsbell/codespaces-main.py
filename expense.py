import json

FILENAME = "expenses.json"

#Function to Load Expenses
def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        return[]
     #  Function to save Expenses
def save_expenses(expenses):
    with open(FILENAME,"w") as file:
        json.dump(expenses,file, indent=4)


def add_expense():
    expenseName = input("Enter expense name:").strip().title()

    while True:
        try:
            amount= float(input("Enter amount: $").strip())
            break
        except ValueError:
            print("Invaild error. Input a number value")

    category= input("Enter a Category").strip().lower()

# MAIN
while True:
    print ("/nSimple Expense Tracker")
    print("1. Add Expense")


    choice = input ("Select an option (1) ").strip()

    if choice == "1":
        add_expense()