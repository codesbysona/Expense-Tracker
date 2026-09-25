def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    print("Expense added successfully!")

    return expense