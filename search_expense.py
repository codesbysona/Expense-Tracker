def search_expense(expenses):
    category = input("Enter category to search: ")
    found = False

    for expense in expenses:
       if expense["category"] == category:
         print("Category:", expense["category"])
         print("Amount:", expense["amount"])
         print("Description:", expense["description"])
         found = True

    if found == False:
        print("Expense not found.")