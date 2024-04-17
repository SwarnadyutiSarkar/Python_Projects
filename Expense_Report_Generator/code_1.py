import csv

# Initialize expense data
expenses = []

# Add a new expense
def add_expense(date, category, description, amount):
    expenses.append({
        'Date': date,
        'Category': category,
        'Description': description,
        'Amount': amount
    })
    print("Expense added successfully!")

# Display all expenses
def display_expenses():
    if not expenses:
        print("No expenses to display.")
        return
    
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Date: {expense['Date']}, Category: {expense['Category']}, Description: {expense['Description']}, Amount: ${expense['Amount']}")

# Generate expense report
def generate_report():
    if not expenses:
        print("No expenses to generate report.")
        return
    
    total_expenses = sum(expense['Amount'] for expense in expenses)
    
    with open('expense_report.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Category', 'Description', 'Amount'])
        writer.writeheader()
        
        for expense in expenses:
            writer.writerow(expense)
        
        writer.writerow({'Date': '', 'Category': '', 'Description': 'Total Expenses', 'Amount': total_expenses})
    
    print("Expense report generated successfully!")

if __name__ == '__main__':
    while True:
        print("\nExpense Report Generator")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (MM/DD/YYYY): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, description, amount)
        
        elif choice == '2':
            display_expenses()
        
        elif choice == '3':
            generate_report()
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")
