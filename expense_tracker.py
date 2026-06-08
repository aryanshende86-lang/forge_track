DATA_FILE = "tracker.txt"

VALID_CATEGORIES = ["food", "transport", "entertainment", "other"]


def add_expense():
    date = input("Date (MM/DD/YY): ").strip()
    
    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("That doesn't look like a valid number. Try again.\n")
        return

    print("Categories: Food / Transport / Entertainment / Other")
    category = input("Category: ").strip().lower()
    if category not in VALID_CATEGORIES:
        print("Not a recognised category, saving as 'Other'.")
        category = "other"

    add_note = input("Add a note? (y/n): ").strip().lower()
    note = input("Note: ").strip() if add_note == "y" else "-"

    with open(DATA_FILE, "a") as f:
        f.write(f"{date},{category.capitalize()},{amount:.2f},{note}\n")

    print("Expense saved!\n")


def print_table(rows):
   
    cw = [10, 15, 10, 30]
    headers = ["Date", "Category", "Amount", "Note"]

    top    = "┌" + "┬".join("─" * (w + 2) for w in cw) + "┐"
    mid    = "├" + "┼".join("─" * (w + 2) for w in cw) + "┤"
    bottom = "└" + "┴".join("─" * (w + 2) for w in cw) + "┘"

    def row_line(cells):
        parts = []
        for cell, w in zip(cells, cw):
            parts.append(f" {str(cell):<{w}} ")
        return "│" + "│".join(parts) + "│"

    print(top)
    print(row_line(headers))
    print(mid)
    for r in rows:
        print(row_line(r))
    print(bottom)


def view_all_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")
        return

    if not lines:
        print("Nothing here yet.\n")
        return

    rows = []
    total = 0.0
    for line in lines:
        date, category, amount, note = line.strip().split(",")
        rows.append([date, category, amount, note])
        total += float(amount)

    print_table(rows)
    print(f"  Total: ₹{total:.2f}\n")


def filter_by_category():
    print("Categories: Food / Transport / Entertainment / Other")
    search = input("Filter by category: ").strip().lower()

    try:
        with open(DATA_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")
        return

    rows = []
    subtotal = 0.0
    for line in lines:
        date, category, amount, note = line.strip().split(",")
        if category.lower() == search:
            rows.append([date, category, amount, note])
            subtotal += float(amount)

    if not rows:
        print(f"No expenses found under '{search.capitalize()}'.\n")
        return

    print_table(rows)
    print(f"  Subtotal ({search.capitalize()}): ₹{subtotal:.2f}\n")


def main():
    print("\n=== Expense Tracker ===\n")
    while True:
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter by category")
        print("4. Exit")
        choice = input("\nChoice: ").strip()

        print()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            print("Bye!\n")
            break
        else:
            print("Invalid option, try again.\n")


main()
