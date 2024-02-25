a = int(input("Enter the no of days: "))
print(a)

year = a/365
print("Total years:",year )
months = (a%365)/30
print("Total months: ",months)
days = ((a%365%30)%7)
print("Total days: ",days)

