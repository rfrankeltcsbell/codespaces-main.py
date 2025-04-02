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
def summarize_expense():
    expenses= load_expenses()

    if not expenses: 
        print("No expenses recorded yet.")
        return 
    
    categories= {}
    for expense in expenses:
        category= expense ["category"]
        amount = expense ["amount"]
        categories [category]= categories.get(category,0 + amount)

    print("\n Expense Summary by Category:")
    for category, total in categories.items():
        print(category +":$" + str(round(total,2)))

def delete_expenses():
    expenses = load_expenses()

    if not expenses: 
        print("No expenses to delete.")
        return

    print("\nYour expenses:")
    for i in range (len(expenses)):
        e = expenses[i]
        print(str(i + 1)+ "."+e["name"]+"-$"+ str(e["amount"]))

        user_input= input("Enter the number of expense we want to delete: ")
    
        if user_input.isdigit():
            index = int(user_input) - 1

            if 0 <= index < len(expenses):
                deleted = expenses.pop(index)
                save_expenses(expenses)
                print("Deleted:"+ deleted["name"]+"-$"+ str(deleted["amount"]))
            else: 
                print("That number does not exist")
        else:  
            print("Please enter a number")
# MAIN
while True:
    print ("/nSimple Expense Tracker")
    print("1. Add Expense")


    choice = input ("Select an option (1-5) ").strip()

    if choice == "1":
        add_expense()
 
    elif choice == "2":
        view_expenses()
    elif choice =="3":
        summarize_expense()
    
    elif choice =="4":
        print("\nGoodbye!")
        break
    elif choice == "5":
        delete_expenses()
    else:
        print("Invaild Choice,Try again")
