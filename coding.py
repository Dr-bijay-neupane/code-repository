def main():
    def calculator(choice):
        a=int(input("ENTER ANY VALUE"))
        b=int(input("ENTER ANY VALUE"))
        match choice:
            case 1:
                return a+b

            case _:
                print("INVALID")
            
    


    c=int(input("Enter value l. ADDING  2.SUBTRACTION 3.MULTIPLICATIN 4.POWER 5.DIVISION"))
    a=calculator(c)
    print(a)

#DUCK TPYING

class PyCharm:
     def execute(self):
        print("OPERATING PYTHON")
    
class laptop:
    def code(self,ide):
        ide.execute()

ide =PyCharm()
lp=laptop()
lp.code(ide)

# operator overloading


a=5
b=6

print(a+b)

# or 

print(int.__add__(a,b))


class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    
    def __add__(self,other):  
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3=student(m1,m2)

        return s3
    
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1=student(56,32)
s2=student(32,44)


s3=s1+s2

print(s3.m1)
print(s3.m2)

if s1>s2:
    print("s1 wins")

else:
    print("s2 wins")

# abstract class

from abc import ABC , abstractmethod

class computer:
    @abstractmethod
    def process(self):
        pass

c=computer()
c.process()

# iterator

nums=[7,53,4,3]


for i in nums:
    print(i)

#or

it = iter(nums)

print(it.__next__)
print(it.__next__)

# or 


print(next(it))


class topten:

    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
        
        else:
            raise StopIteration

        return val
    
values=topten()

for i in values:
    print(i)

# exception errors

a=5
b=4

try:
    print("resource open")
    print(a/b)

    k=int(input("ENTER VLAUE"))
    print(k)
  
except ZeroDivisionError as e :         #exception or ZeroDivisioinError
    print("YOU ARE TRYING TO DIVIDE A NUMBER BY ZERO",e)

except ValueError as e :
    print("INVALID VALUE")

except Exception as e :
    print("ERROR!!")
    
finally:
    print("resource closed")

    #multi threading 

from time import sleep
from threading import *

class hello(Thread):  #thread does parrel work
    def run(self):
        for i in range(5):
            print("HELLO")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("HI")
            sleep(1) #delay by 1 second

a=hello()
b=hi()

a.start()
sleep(0.2)
b.start()   #start calls run method/function internally tho run is the name of method


a.join()
b.join()   #doesnt let until a and b finished

print("bye")