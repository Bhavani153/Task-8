#1
class circle:
    def __init__(self):
        self.a=[10,501,22,37,100,999,87,351]
    def read_number(self):
        print(self.a)
obj=circle()
obj.read_number()

#2
class myclass:
    pi=3.141
    def priv_var(self):
        print("i am inside class myclass")
    def a(self):
        print("private variable value=",myclass.pi)
obj=myclass()
obj.a()

#3
class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
newcircle=circle(10)
print("Area & Perimeter:")
print(newcircle.area())
print(newcircle.perimeter())