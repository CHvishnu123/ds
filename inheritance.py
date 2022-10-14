class rec(shapes):
    def _init_(self):
        shapes.__init_(self,3)
    def findArea(self):
        a,b=self.sides
        area=(a+b)*2
        print("the area of the rectangle is"%area)
a=int(input("enter the length of a rectangle:"))
b=int(int(input("enter the breadth of rectangle:"))
    
    