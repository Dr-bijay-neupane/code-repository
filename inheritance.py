
class A:

    def __init__(self):
        print("OPERATING from CLASS A")
        

    def feature(self):
        print("FEATURE 1")


    def feature2(self):
        print("FEATURE 2")


class B(A):

    def __init__(self):
        super( ).__init__()
        print("OPERATING from CLASS B")

    def feature3(self):
        print("FEATURE 3")

class C(B):

    def __init__(self):
        super().__init__()
        print("OPERATING FROM C")

    def feature4(self):
        print("FEATURE 4")

ob=A()
ob.feature()
ob.feature2()

ob1=B()
ob1.feature()
ob1.feature2()

ob1.feature3()

ob2=C()
ob2.feature4()


# over-riding

class A:
    def show(self):
        print("OPRATING FROM A")
    
class B(A):

    def show(self):
        print("OPERATING FROM B")

a=B()
a.show()