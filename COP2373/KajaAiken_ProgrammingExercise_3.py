# This program will track a user's expenses using the reduce and lambda within a function.
# The user's input will be stored in specific lists. At the end, the program will display
# the user's total, highest, and lowest expenses.


# Define the reduce functools.
from functools import reduce

# Define the monthly expenses function.
def user_expenses():
    print('-' * 50)
    print('              Monthly Expense Report')
    print('-' * 50)
    expenses = []

    # Prompt the user to get data.
    while True:
        expense_type = input('Please enter the type of expense you would like to track: \n'
                             'When you are finished, please enter DONE. \n').strip()
        if expense_type.lower() == 'done':
            break

        try:
            amount = float(input(f'Please enter the amount you would like to track for {expense_type}: \n'))
            if amount <= 0:
                print('Please enter a positive number.')
                continue

            # Put the input in a dictionary to track.
            expenses.append([expense_type, amount])
        except ValueError:
            print('Please enter a numeric value.')

    return expenses


def track_expenses(expenses):
    # Initiate usage of reduce and lambda to sum all total expenses.
    total_expenses = reduce(lambda total, expense: total + expense[1], expenses, 0)

    # Track the highest expense.
    highest_expense = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Track the lowest expense.
    lowest_expense = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    return total_expenses, highest_expense, lowest_expense

def main():
    # Pull the data.
    expenses = user_expenses()

    # Ensure that the user has put data in.
    if not expenses:
        print('There are no expenses. Goodbye!')
        return

    # Categorize the data.
    total_expense, highest_expense, lowest_expense = track_expenses(expenses)

    # Display the total of all expenses to the user.
    print('\n')
    print('=' * 50)
    print(f'Here is your total monthly expenses: ${total_expense:,.2f}')
    print(f'Your highest monthly expense is {highest_expense[0]}: ${highest_expense[1]:,.2f}')
    print(f'Your lowest monthly expense is {lowest_expense[0]}: ${lowest_expense[1]:,.2f}')
    print('=' * 50)

if __name__ == '__main__':
    main()
