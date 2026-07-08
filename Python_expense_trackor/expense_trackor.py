total = 0 
def main():
    global total
    while True:
        expense = input("Enter an expense (or type 'Exit' to quit):")
        if expense.lower() == 'exit':
            break
        try:
            total += float(expense)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"Total expenses: ${total:.2f}")
if __name__ == "__main__":
    main()