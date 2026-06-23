import json

def load_data():
    try:
        with open("budget_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": 0, "expenses": []}

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def add_income(data):
    income = float(input("Enter monthly income: $"))
    data["income"] = income
    print("Income added successfully.")

def add_expense(data):
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: $"))

    expense = {
        "name": name,
        "amount": amount
    }

    data["expenses"].append(expense)
    print("Expense added successfully.")

def view_summary(data):
    total_expenses = sum(item["amount"] for item in data["expenses"])
    remaining = data["income"] - total_expenses

    print("\n----- Budget Summary -----")
    print(f"Monthly Income: ${data['income']:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining:.2f}")

    print("\nExpenses:")
    for expense in data["expenses"]:
        print(f"- {expense['name']}: ${expense['amount']:.2f}")

def main():
    data = load_data()

    while True:
        print("\nSMART BUDGET MANAGER")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income(data)

        elif choice == "2":
            add_expense(data)

        elif choice == "3":
            view_summary(data)

        elif choice == "4":
            save_data(data)
            print("Data saved.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()