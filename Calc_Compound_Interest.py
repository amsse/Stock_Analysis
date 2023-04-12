# User Inputs

    # Principal:
P = float(input("Starting ammount is: "))

    # Annual Interest Rate:
AIR = float(input("Annual interest is: "))

    # Compounding Rate (in days):
CR = int(input("Number of days the investment compounds is: "))

    # Duration:
D = float(input("The duration in years for the investment is: "))


# Formulas:
total = P * (((1 + (AIR/(100.0 * CR))) ** (CR*D)))
pct_return = int(((total*100)/P)-100)

# Displays the final amount after the given number of years:
print("The investment has generated a compounded return of: " + str(total))
print("The total return for the investment is " + str(pct_return) + "%")
