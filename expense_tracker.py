total = 0
count = 0

while True:
    expense = input("Enter expense (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative.")
            continue

        total += expense
        count += 1

    except ValueError:
        print("Please enter a valid number.")
        continue

if count > 0:
    average = total / count
else:
    average = 0

print("\nExpense Summary")
print("---------------")
print("Number of Expenses:", count)
print("Total Spent:", total)
print("Average Expense:", round(average, 2))