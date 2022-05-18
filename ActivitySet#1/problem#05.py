score = input("Enter Score: ")

try:
  f_score=float(score)
  while f_score>=0.0 and f_score<=1.0:
    if f_score>=0.9:
      print("A")
      break
    elif f_score>=0.8:
      print("B")
      break
    elif f_score>=0.7:
      print("C")
      break
    elif f_score>=0.6:
      print("D")
      break
    elif f_score<0.6:
      print("F")
      break
except:
  print("Grade is out of range")

  