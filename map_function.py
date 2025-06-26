a=[1,2,3,4,5]
b=[4,5,6,7,8,9]
c=list(map(lambda x,y:x+y,a,b))
print(c)
d=list(map(lambda x:x*x,a))
print(d)
g="gali sateesh"
k=g.split(' ')
e=list(map(lambda x:(x,len(x)),k))
print(e)
o=list(map(int,input().split()))
print(o)
