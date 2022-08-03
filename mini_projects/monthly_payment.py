def monthly_payment(principal, annual_interest_rate, duration):
    r = (annual_interest_rate/100)/12
    n = duration*12
    if annual_interest_rate == 0:
        mp = principal/n
    else:
        soorat = principal * (r*(1+r)**n)
        makhraj = ((1+r)**n )- 1
       #monthly_payment
        mp = soorat / makhraj
    return mp
