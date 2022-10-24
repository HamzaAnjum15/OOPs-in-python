class calculator:
    def __init__(self,num):
        self.number= num
    def square(self):
        print(f"the square of {self.number} is {self.number **2}")
    def cube(self):
        print(f"the cube of {self.number} is {self.number **3}")
    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number **0.5}")
    @staticmethod
    def greet():
        print("welcome to the best calculator in the world")
a=calculator(3)
a.greet()
a.square()
a.cube()
a.squareroot()
