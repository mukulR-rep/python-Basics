#Write a program to find the simple interest and compound interest?
def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100),time))
    return result
def simple_interest(principle, rate, time):
    result = (principle * rate * time)/100
    return result

p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate:" ))
t = float(input("Enter the time in years: "))
amount = compound_interest(p, r, t)
interest = amount - p
simple_int = simple_interest (p, r, t)

print("Compound amount is %.2f " % amount)
print("Compound interest is %.2f " % interest)
print("Simple interest is %.2f " % simple_int)
