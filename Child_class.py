#perent class in oops_demo file
from Oops_Demo import Calculator


class ChildIm(Calculator):
    num2 = 100

    def __init__(self):
        Calculator.__init__(self, 10, 20)

    def total(self):
        return self.num2 + self.num + self.Summation()
    def Devidedbytwo(self):
        return self.total() / 2

obj = ChildIm()
print(obj.total())

print(obj.Devidedbytwo())