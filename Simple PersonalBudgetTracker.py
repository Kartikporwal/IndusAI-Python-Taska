import json

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, transaction_type):
        transaction = {
            'amount': amount,
            'category': category,
            'type': transaction_type
        }
        self.transactions.append(transaction)

    def view_transactions(self):
        for idx, transaction in enumerate(self.transactions, 1):
            print(f"{idx}. {transaction['type'].capitalize()}: ${transaction['amount']} in {transaction['category']}")

    def save_transactions(self, filename='transactions.json'):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file)
        print("Transactions saved successfully.")

    def load_transactions(self, filename='transactions.json'):
        try:
            with open(filename, 'r') as file:
                self.transactions = json.load(file)
            print("Transactions loaded successfully.")
        except FileNotFoundError:
            print("No saved transactions found.")

    def get_summary(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = income - expenses
        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expenses}")
        print(f"Balance: ${balance}")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Get Summary")
        print("5. Save Transactions")
        print("6. Load Transactions")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            budget_tracker.add_transaction(amount, category, 'income')
        elif choice == '2':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            budget_tracker.add_transaction(amount, category, 'expense')
        elif choice == '3':
            budget_tracker.view_transactions()
        elif choice == '4':
            budget_tracker.get_summary()
        elif choice == '5':
            budget_tracker.save_transactions()
        elif choice == '6':
            budget_tracker.load_transactions()
        elif choice == '7':
            print("Exiting the budget tracker. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
