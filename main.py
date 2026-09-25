from add_expense import add_expense
from view_expense import view_expenses
from analysis import analyze_expenses
from search_expense import search_expense
from budget import check_budget
 
expenses = []

while True:
    expense = add_expense()
    expenses.append(expense)

    choice = input("Do you want to add another expense? (yes/no): ")

    if choice == "no":
        break

analyze_expenses(expenses)
search_expense(expenses)
view_expenses(expenses)
check_budget(expenses)