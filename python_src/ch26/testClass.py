#coding=utf-8
class FirstClass:  #在类嵌套的代码块中顶层的赋值的任何变量都会变成类的属性
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)
        
      
class SecondClass(FirstClass):
    def display(self):    #有时候我们把这种在树中较低处发生的重新定义的、取代属性的动作叫做重载
        print('Current value= "%s"' % self.data)  
        
        
class ThirdClass(SecondClass):
    def __init__(self,value): 
        self.data=value
    def __add__(self,other): 
        return ThirdClass(self.data+other)   
    def __str__(self):   
        return '[ThirdClass:%s]' % self.data
    def mul(self,other):
        self.data *= other
        
        
if __name__ == "__main__":
    x=FirstClass()
    y=FirstClass()
    x.setdata("King Arthur")
    y.setdata(3.14159)
    x.display()
    y.display()
    
    x.data="外部赋值"
    x.display()
    x.autovariable="autovariable"
    print(x.autovariable)
    
    z=SecondClass()
    z.setdata(42)
    z.display()
    
    a=ThirdClass('abc')
    a.display()
    print(a)
    b=a+'xyz'
    b.display()
    print(b)
    a.mul(3)
    print(a)
    
    