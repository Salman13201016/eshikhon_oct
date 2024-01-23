class Car:
    name = ''
    color =''
    c1 = ''
    c2 = ''

    def __init__(self,x1,x2):
        self.c1 = x1
        self.c2 = x2
        # print("Check the car")

    def operation(self):
        return self.color
    def check(self):
        return self.c1,self.c2

class Car2(Car):
    pass


obj3 = Car2('check1','check2')
check_V1,check_v2 = obj3.check()
print(check_V1,check_v2)

# obj1 = Car('check1','check2')
# check_V1,check_v2 = obj1.check()

# print(check_V1,check_v2)


# obj1.name="Toyota xyz"
# obj1.color = 'blue'

# obj2 = Car()
# obj2.name = "Mazda xyz"
# obj2.color = "yellow"

# print(obj1.operation())
# print(obj1.name,obj1.color)

# print(obj2.name,obj2.color)

