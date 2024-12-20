import json

# File to store expense data
EXPENSE_FILE = "expenses.json"

# Load existing expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file)

# Add a new expense
def add_expense(expenses):
    category = input("Enter category (e.g., food, transport, entertainment): ")
    amount = float(input("Enter amount: "))
    note = input("Add a note (optional): ")
    expenses.append({"category": category, "amount": amount, "note": note})
    print("Expense added successfully!")
    return expenses

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Here are your expenses:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['category']} - ${expense['amount']} (Note: {expense['note']})")

# Get summary of expenses by category
def expense_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    print("Expense Summary by Category:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

# Main program loop
def main():
    print("Welcome to the Personal Expense Tracker!")
    expenses = load_expenses()

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            expenses = add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            expense_summary(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()