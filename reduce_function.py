from functools import reduce
a=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,a)
print(sum)
maxval=reduce(lambda x,y:x if x>y else y,a)
print(maxval)
