def check_budget(expenses):

    budget = float(input("Enter your monthly budget: "))

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense:", total)

    if total > budget:
        print("Budget exceeded!")
    else:
        print("You are within your budget.")