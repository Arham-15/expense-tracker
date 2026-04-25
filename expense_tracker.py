expense = [] 
while True:
    print("1. Add Expenses\n2. View Expenses\n3. Show Total Expense\n4. Exit")
    n = int((input("CHOOSE OPTION (1-4)  ")))
    if n == 1:
        (print("Enter all expenses and press '0' for next"))
        values = float(input())
        while values != 0:
            expense.append(values)
            values = float(input())
    elif n == 2:
        for i, each in enumerate(expense):
            print(i+1,each)    
    elif n == 3:
        s = sum(expense)
        print("Total expense is:",s)
    elif n == 4:
        print("EXIT")
        break
    else :
        print("INVALID INPUT")
