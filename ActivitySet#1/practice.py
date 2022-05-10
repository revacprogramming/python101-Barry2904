import datetime
def WhenShouldIcode():
     return datetime.date.today()

def my_input():
  my_name=input("What is your name")
  return my_name

def output(name,date):
    print(f"{name} should code on {date}")

def main():
    name=my_input()
    date = WhenShouldIcode()
    output(name,date)
main()