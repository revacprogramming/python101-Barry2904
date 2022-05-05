# Conditional Execution


# 3.1
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
 	print(h*r)
elif h > 40:
	print(40*r+(h-40)*1.5*r)

#3.3
  
score = input("Enter Score: ")
f_score=float(score)
if f_score>=0.0 and f_score<=1.0:
    if f_score>=0.9:
        print("A")
    elif f_score>=0.8:
        print("B")
    elif f_score>=0.7:
        print("C")
    elif f_score>=0.6:
        print("D")
    elif f_score<0.6:
        print("F")
else:
    print("Grade is out of range")