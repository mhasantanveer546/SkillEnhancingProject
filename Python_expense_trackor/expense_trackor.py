total = 0 
expense = []
def main():
    global total
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
                total += amount
                expense.append({"description": expense_description, "amount": amount})
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    print(f"Total expenses: ${total:.2f}")
    print("Expenses:")
    for i, expenses in enumerate(expense, 1):
        print(f"{i}. {expenses['description']}: ${expenses['amount']:.2f}")

if __name__ == "__main__":
    main()