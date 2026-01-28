print("Welcome to the Tax Calculator")
salary = float(input("Please enter your salary to calculate tax: "))

if salary < 6000:
    tax_rate = 0.10
elif salary < 15000:
    tax_rate = 0.15
else:
    tax_rate = 0.20

tax_amount = salary * tax_rate
print("Your tax amount is:", tax_amount)