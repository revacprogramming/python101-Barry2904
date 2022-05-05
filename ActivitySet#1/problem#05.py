# Functions

def computepay(h,r):
    return 40*r+(h-40)*1.5*r

hrs = input("Enter Hours:")
h=float(hrs)
rate= input("Enter Rate")
r=float(rate)
if h>40:
    p = computepay(h,r)
elif h<=40:
    p=h*r
print("Pay", p)