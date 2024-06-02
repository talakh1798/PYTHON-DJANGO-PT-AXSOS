# Name:Tala khaled
# Email:talakh1798@gmail.com
# desc: creating a class and creating new instances , chaining methods and writing flexible functions that can take a varying number of arguments
 
class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self

    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

md = MathDojo()
print(md.add(2).result)
print(md.add(2,5).result)
print(md.add(8,2,-1).result)


md = MathDojo()
print(md.subtract(3).result)
print(md.subtract(2,1).result)
print(md.subtract(6, 2, -1).result)

# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)	
