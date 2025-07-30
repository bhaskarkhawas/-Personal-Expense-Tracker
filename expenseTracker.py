import json
import os
from datetime import datetime
from collections import defaultdict

# File name to store expenses
DATA_FILE = "expenses.json"

# Load expenses from a JSON file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save expenses to a JSON file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense entry
def add_expense(expenses):
    try:
        amount = float(input("Enter amount (e.g., 50.00): "))
        category = input("Enter category (e.g., Food, Travel): ").strip().title()
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        date = date_str if date_str else datetime.today().strftime("%Y-%m-%d")

        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a valid number.\n")

# Display a summary of all expenses
def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = 0
    category_summary = defaultdict(float)
    monthly_summary = defaultdict(float)

    for exp in expenses:
        total += exp["amount"]
        category_summary[exp["category"]] += exp["amount"]
        month = exp["date"][:7]  # Extract YYYY-MM for monthly summary
        monthly_summary[month] += exp["amount"]

    print("\nExpense Summary:")
    print(f"Total Spending: {total:.2f}")

    print("\nSpending by Category:")
    for cat, amt in category_summary.items():
        print(f"{cat}: {amt:.2f}")

    print("\nMonthly Spending:")
    for month, amt in sorted(monthly_summary.items()):
        print(f"{month}: {amt:.2f}")
    print()

# Show all expenses with index
def list_expenses(expenses):
    for idx, exp in enumerate(expenses):
        print(f"{idx + 1}. {exp['amount']} - {exp['category']} on {exp['date']}")
    print()

# Edit an existing expense
def edit_expense(expenses):
    if not expenses:
        print("No expenses to edit.\n")
        return

    list_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to edit: ")) - 1
        if 0 <= index < len(expenses):
            exp = expenses[index]
            print("Leave blank to keep the current value.")

            amount = input(f"New amount ({exp['amount']}): ")
            category = input(f"New category ({exp['category']}): ")
            date = input(f"New date ({exp['date']}): ")

            if amount:
                exp["amount"] = float(amount)
            if category:
                exp["category"] = category.strip().title()
            if date:
                exp["date"] = date.strip()

            save_expenses(expenses)
            print("Expense updated successfully.\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

# Delete an expense
def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.\n")
        return

    list_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses(expenses)
            print(f"Deleted: {deleted['amount']} - {deleted['category']} on {deleted['date']}\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

# Main menu-driven interface
def main():
    print("Personal Expense Tracker\n")
    expenses = load_expenses()

    while True:
        print("Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Exiting... Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()

#Assignment submutted by Bhaskar Khawas, stud id: STU68232718021b21747134232