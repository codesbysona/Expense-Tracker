def analyze_expenses(expenses):

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nExpense Analysis:")
    print("Total Expense:", total)

    category_total = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] = category_total[category] + amount
        else:
            category_total[category] = amount

    print("\nCategory-wise Expense:")

    for category in category_total:
        print(category, ":", category_total[category])