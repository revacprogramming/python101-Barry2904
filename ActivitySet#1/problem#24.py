# def f(a=2,b=3,c=4):
#   return a+b+c
# print(f(c=5))

# def f(*args):
#   print(args,*args)
# f(1,2,3,4)

# def test():
#   print()
# t=(1,2)
# test(*t)

def f(*args,**kwargs):
  print(args,*args,kwargs,**kwargs)
f(1,2,3)