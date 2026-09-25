# Problem Statement

Managing daily expenses manually can make it difficult to keep track of spending and understand where money is being used. A simple expense tracker can help users record their expenses, view them, analyse spending by category, search for specific expenses, and check their spending against a budget.

## Objectives

- To create a simple Python-based expense tracker.
- To record and view daily expenses.
- To calculate total and category-wise expenses.
- To search for expenses by category.
- To compare total expenses with a given budget.

## Functional Requirements

1. **Add Expense** – The user can enter the category, amount, and description of an expense.
2. **View and Analyse Expenses** – The system can display all expenses and calculate total and category-wise expenses.
3. **Search Expense** – The user can search for expenses using a category.
4. **Budget Check** – The system compares the total expense with the user's budget.

## Non-Functional Requirements

1. **Usability** – The program should be simple and easy to use.
2. **Reliability** – The program should give correct results for the entered expenses.
3. **Maintainability** – The code should be divided into separate modules for easier maintenance.
4. **Error Handling** – The program should handle incorrect inputs without stopping unexpectedly.

## Architecture / Workflow

1. The user enters expense details.
2. The expense is added to the expense list.
3. The user can view all recorded expenses.
4. The system calculates the total and category-wise expenses.
5. The user can search for an expense by category.
6. The system compares the total expense with the entered budget.

## Subject Concepts Used

- Variables
- Input and output
- Data types
- Operators
- Conditional statements
- For loops
- While loop
- Lists
- Dictionaries
- Functions
- Modules and imports

## Testing

The project was tested using different expense entries and budget values to check whether all modules work correctly.

- Tested adding multiple expenses.
- Tested displaying all expenses.
- Tested total and category-wise calculation.
- Tested searching for an existing category.
- Tested searching for a category that does not exist.
- Tested the budget check with expenses below and above the budget.

## Project Structure

- `main.py` – Controls the main program flow.
- `add_expense.py` – Adds a new expense.
- `view_expense.py` – Displays all expenses.
- `analysis.py` – Calculates total and category-wise expenses.
- `search_expense.py` – Searches expenses by category.
- `budget.py` – Checks expenses against the budget.