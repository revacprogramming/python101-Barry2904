class fibo:
  def __init__(self):
    self.a=0
    self.b=1
  def __next__(self):
    yield self.a
    self.a=self.b
    self.b=self.b+self.a
    return self.a
x=fibo()
print(x)
# for i in x:
#   yield i