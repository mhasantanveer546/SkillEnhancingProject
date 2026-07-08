import sqlite3
def create_database():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  description TEXT NOT NULL,
                  amount REAL NOT NULL)''')
    conn.commit()
    conn.close()

def insert_expense(description, amount):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (description, amount))
    conn.commit()
    conn.close()
    
def get_all_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT description, amount FROM expenses")
    rows = c.fetchall()
    conn.close()
    return rows


def main():
    create_database()
    while True:
        expense_description = input("Enter an expense description (or type 'Exit' to quit):")
        if expense_description.lower() == 'exit':
            break
        while True:
            expense_amount = input("Enter an expense amount:")
            try:
                amount = float(expense_amount)
                if amount < 0:
                    print("Amount cannot be negative. Please enter a valid number.")
                    continue
                insert_expense(expense_description, amount)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    all_expenses = get_all_expenses()
    grand_total = sum(amount for description, amount in all_expenses)

    print(f"Total expenses: ${grand_total:.2f}")
    print("Expenses:")
    for i, (description, amount) in enumerate(all_expenses, 1):
        print(f"{i}. {description}: ${amount:.2f}")

if __name__ == "__main__":
    main()