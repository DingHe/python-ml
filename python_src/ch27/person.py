#coding=utf-8
class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay*(1+percent))
        
    def __str__(self):
        return '[Person:%s,%s]' % (self.name,self.pay)
    
    
    
class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent,bonus=.10):
        Person.giveRaise(self, percent+bonus)    
    
    
    
    
    

if __name__ == '__main__':
    bob=Person('Bob Smith')
    sue=Person('Sue Jone',job='dev',pay=100000)
    print(bob.name,bob.pay)
    print(sue.name,sue.pay)
    print(bob.lastName(),sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)
    
    tom=Manager('Tom Jones',50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    
    print('--All three--')
    for object in (bob,sue,tom):
        object.giveRaise(.10)
        print object
    
    print('__X__')
    print(tom.__class__.__name__)
    print(tom.__class__.__bases__)
    print(tom.__dict__.keys())
    