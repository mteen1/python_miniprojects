from monthly_payment import *
from remaining_loan import *

# main program
principal = float(input("Enter loan amount:"))
annual_interest_rate = float(input("Enter annual interest rate (percent): "))
duration = int(input("Enter loan duration in years: "))

mp = monthly_payment(principal, annual_interest_rate, duration)

print("LOAN AMOUNT:", int(principal), "INTEREST RATE (PERCENT):", int(annual_interest_rate))

print("DURATION(YEARS):", duration, "MONTHLY PAYMENT:", int(mp))
for i in range(1, (duration + 1)):
    tp = mp * i * 12
    rm = remaining_loan(principal, annual_interest_rate, duration, i * 12)
    print("YEAR:", i, "BALANCE:", int(rm), "TOTAL PAYMENT:", int(mp * i * 12))
