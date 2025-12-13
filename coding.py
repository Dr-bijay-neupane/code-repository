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