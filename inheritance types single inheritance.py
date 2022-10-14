class parent:
    def func1(self):
        print("this funtion is parent class")
class Child(parent):
    def func2(self):
        print("this function is child class")
object=Child()
object.func1()
object.func2()
