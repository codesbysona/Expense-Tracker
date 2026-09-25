def view_expenses(expenses):

    print("\nAll Expenses:")

    for expense in expenses:
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print("Description:", expense["description"])
        print("--------------------")