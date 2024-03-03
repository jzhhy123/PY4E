def computepay(h, r):
    Hours = float(hrs)
    Rate = float(rate)
    if 0 <= Hours <= 40:
        Pay = Hours * Rate
        return Pay
    if Hours > 40:
        Pay = 40 * Rate + (Hours - 40) * (1.5 * Rate)
        return Pay

hrs = input('Enter Hours:')
rate = input('Enter Rate:')
p = computepay(hrs, rate)
print("Pay", p)