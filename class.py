class computer:
     
    college="ACEM"
    def __init__(self):
        self.name="bijay"
        self.age=21
        self.lap=self.laptop()

    class laptop:

        def __init__(self):
            self.brand="asus vivebook"
            self.cpu="12000H i5"
            self.ram=16

        def show(self):
            print(self.brand,self.cpu,self.ram)
ob1=computer()
ob2=computer()
ob1.name="ramu"
ob1.college="ACEM"
print(ob1.name)
print(ob1.age)
print(ob1.college)
print(ob2.name)
print(ob2.age)
print(ob2.college)



lp1=computer.laptop()
lp1.show()


class computer:
    def config():
        print("16gb ram,1tb storage")
comp1=computer()
computer.config()
print("hi")