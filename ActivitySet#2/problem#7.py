# Hint: operator overloading special methods (__add__, __sub__, etc.)
class Menu:
    def __init__(self,x='',y=''):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x + other.x ,self.y + other.y

#==============METHOD 1==========
a= Menu("idly ", 'vada ')
b= Menu("10", '20')
c=a+b
for i in c:
    print(i)
#==============METHOD 2==========
m = Menu("idly ", 'vada ') + Menu("10", '20')
print(m)  

