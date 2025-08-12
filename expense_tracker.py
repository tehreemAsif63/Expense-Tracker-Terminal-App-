# ask for input price and category
# enter daily expenses input price and categfory
# add to total and category
# save that in list
# do you wnat to enter more?
# if yes again
# if no leave
# show total expoense
# show catgeory wise expense


print("Hello and Welcome to the Expense Tracker Terminal")
expenses = []
total = 0

while True:
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    total += amount
    if input("Do you want to enter more? y/n?").lower() == "n":
        break
print(f"Total expense: {total}")
