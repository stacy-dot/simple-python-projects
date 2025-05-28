print("Here's a calculator to help you decide the total amount to leave as you tip your waiter!")

tip_percentage=float(input("Enter the tip %:"))
bill=float(input("Enter the bill:"))
people=int(input("Enter the number of people:"))

tip=bill*(tip_percentage/100)
total=tip+bill
amountpp=total/people

print(f"Each person will pay {amountpp}")
