class parent:
    def func1(self):
        print("this funtion is parent class")
class child1(parent):
    def func2(self):
        print("this funtion is parent child1")
        
class child2(parent):
    def func3(self):
        print("this funtion is parent child2")
object1=child1()
object2=child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

        
