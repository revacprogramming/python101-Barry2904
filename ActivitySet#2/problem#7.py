class Menu:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x + other.x ,self.y + other.y
        '''
        x = self.x + other.x
        y = self.y + other.y
        return Menu(x,y)'''

# m = Menu()
a= Menu("idly ", 'vada ')
b= Menu("10", '20')
# m = m + Menu("idly", '10') + Menu("vada", '20')  
# Hint: operator overloading special methods (__add__, __sub__, etc.)
c=a+b
for i in c:
    print(i)
