
import csv
from datetime import datetime
from pathlib import Path

CSV_FILE = Path(__file__).with_name("expenses.csv")

FIELDNAMES = ["date", "category", "description", "amount"]



def load_expenses():
    if not CSV_FILE.exists():
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
        return []

    expenses = []

    with open(CSV_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames:
            reader.fieldnames = [
                name.strip().lower() for name in reader.fieldnames
            ]

        print("CSV columns found:", reader.fieldnames)

        for line_number, row in enumerate(reader, start=2):
            try:
                date = row["date"].strip()
                category = row["category"].strip()
                description = row["description"].strip()
                amount = float(row["amount"])

                datetime.strptime(date, "%Y-%m-%d")

                if amount < 0:
                    raise ValueError("Amount cannot be negative")

                expenses.append({
                    "date": date,
                    "category": category,
                    "description": description,
                    "amount": amount
                })

            except (ValueError, TypeError, KeyError, AttributeError) as error:
                print(f"Line {line_number}: {error} | Data: {row}")

    return expenses


def save_expense(expense):
    file_exists = CSV_FILE.exists() and CSV_FILE.stat().st_size > 0

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(expense)


def get_valid_date():
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def get_valid_amount():
    while True:
        amount_text = input("Enter amount: ").strip()

        try:
            amount = float(amount_text)

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Enter a number.")


def add_expense():
    print("\n--- Add Expense ---")

    date = get_valid_date()

    categories = ["Food", "Travel", "Study", "Bills", "Fun"]
    print("Categories:", ", ".join(categories))

    category = input("Enter category: ").strip().title()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip().title()

    description = input("Enter description: ").strip()

    while not description:
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    amount = get_valid_amount()

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}"
    }

    save_expense(expense)
    print("Expense saved successfully!")


def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n{:<12} {:<12} {:<25} {:>12}".format(
        "Date", "Category", "Description", "Amount"
    ))
    print("-" * 65)

    for expense in expenses:
        print("{:<12} {:<12} {:<25} {:>12.2f}".format(
            expense["date"],
            expense["category"],
            expense["description"][:25],
            expense["amount"]
        ))


def view_all_expenses():
    print("\n--- All Expenses ---")
    display_expenses(load_expenses())


def filter_expenses():
    expenses = load_expenses()

    print("\n--- Filter Expenses ---")
    print("1. Filter by category")
    print("2. Filter by month (YYYY-MM)")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        category = input("Enter category: ").strip().casefold()

        filtered = [
            expense for expense in expenses
            if expense["category"].casefold() == category
        ]

    elif choice == "2":
        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month. Use YYYY-MM, for example 2026-10.")
            return

        filtered = [
            expense for expense in expenses
            if expense["date"][:7] == month
        ]

    else:
        print("Invalid choice.")
        return

    display_expenses(filtered)


def show_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses available for summary.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + expense["amount"]
        )

    print("\n--- Category Summary ---")

    for category, total in sorted(category_totals.items()):
        print(f"{category}: {total:.2f}")

    grand_total = sum(expense["amount"] for expense in expenses)
    biggest_expense = max(expenses, key=lambda expense: expense["amount"])

    print("-" * 35)
    print(f"Grand total: {grand_total:.2f}")
    print(
        f"Biggest expense: {biggest_expense['description']} "
        f"({biggest_expense['category']}) - "
        f"{biggest_expense['amount']:.2f}"
    )


def main():
    load_expenses()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Summary")
        print("5. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()
