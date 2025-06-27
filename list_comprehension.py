b=[1,2,3,4,5]
a=[i*i for i in b]
print(a)#[1,4,9,16,25]
c=[i*i for i in b if i%2==0]
print(c)#[4,16]
d=[i for i in b if i not in a]
print(d)#[2,3,5]

