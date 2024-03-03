hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the Hourly Rate:")
r = float(rate)
if 0<= h <= 40:
    Pay=h*r
elif h>40:
    Pay=40*r+(h-40)*(r*1.5)
print(Pay)