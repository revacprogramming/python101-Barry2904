# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

# hrs = input("Enter Hours:")
# rate= input("Enter Rate per Hour")
# pay= float(rate)* float(hrs)
# print("Pay:",pay) 

def compute(hr,rate):
  pay=float(rate)*float(hr)
  return pay

def output(total):
  print("The Gross pay is:-",total)

def main():
  global hr,rate
  hr=input("Enter hours:- ")
  rate=input("Enter the rate:- ")

main()
total=compute(hr,rate)
output(total)