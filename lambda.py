list1=[3,4,10,9,18,66,13,15]
# def isEven(i):
#     return i%2==0

evenNum=list(filter(lambda i: i>5,list1))
print(evenNum)

cubeNum=list(map(lambda i:i**3,list1))
print(cubeNum)

# To swap lowerCase to UpperCase and vice-versa...
list2=["a","B","c","D","e","f"]
alpha=list(map(lambda i:i.swapcase(),list2))
print(alpha)

# reduce ...
from functools import reduce
list1=[1,2,3,4,5,6]
sum =reduce(lambda i,j:i+j,list1)
print(sum)
