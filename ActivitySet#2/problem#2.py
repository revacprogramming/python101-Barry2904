def add(a,b):
  return int(a)+int(b)

def output(a,b,sum):
  print(a,"+",b,"is",sum)

def main():
    a,b=input("Enter two numbers:- ").split()
    sum=add(a,b)
    output(a,b,sum)


if __name__ == '__main__':
    main()
