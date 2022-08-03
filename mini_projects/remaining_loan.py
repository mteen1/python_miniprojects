# nop is number of payments
def remaining_loan(principal, annual_interest_rate, duration, nop):
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    if annual_interest_rate == 0:
        rl = principal - (principal * (nop / n))
    else:
        soorat = principal * (((1 + r) ** n) - (1 + r) ** nop)
        makhraj = ((1 + r) ** n) - 1
        rl = soorat / makhraj
    return rl
