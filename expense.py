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
    expenseName= input(" Enter expense payroll").strip().title()
    expenseName= input("Enter expense bank fees").strip().title()
    expenseName= input("Enter expense advertising").strip().title()
    while True:
        try:
            amount= float(input("Enter amount: $").strip())
            break
        except ValueError:
            print("Invaild error. Input a number value")

    category= input("Enter a Category").strip().lower()
    categories = {"food":"Food","transportation":"Transportation","banking":"Banking","other":"Other"}
    categories = categories.get(category,"Other")

    expenses = load_expenses()
    expenses.append({"name":expenseName,"amount":amount,"category":category})
    save_expenses(expenses)

    print("Expense " + expenseName + "added successfully!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded")
        return
    print("\nYour expenses:")
    for expense in expenses:
        print(expense["name"]+ "-$"+ str(expense["amount"]) + expense["category"])

# MAIN
while True:
    print ("/nSimple Expense Tracker")
    print("1. Add Expense")


    choice = input ("Select an option (1) ").strip()

    if choice == "1":
        add_expense()
   