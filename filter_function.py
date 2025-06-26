a=[1,2,3,4,5,6,7,8]
b=[2,4,6,8,9]
c=list(filter(lambda x:(x%2==0),a))
print(c)
d=list(filter(lambda x:x%3==0,a))
print(d)
e=list(filter(lambda x:x in a,b))
print(e)
f=list(filter(lambda x:x%2==0,[1,2,3,4,5]))
print(f)
