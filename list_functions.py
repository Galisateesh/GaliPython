a=[1,2,1,1,1,1,3,4,[1,2,3],1]
print(len(a))#10
print(a.count(1))#6
print(a.index(3))#6
print(len(a[8]))#3
print(a[8][1])#2
a.append(10)
print(a)#[1, 2, 1, 1, 1, 1, 3, 4, [1, 2, 3], 1, 10]
a.extend([100])
print(a)#[1, 2, 1, 1, 1, 1, 3, 4, [1, 2, 3], 1, 10, 100]
a.insert(2,15)
"""insert(index number,index value)"""
print(a)#[1, 2, 15, 1, 1, 1, 1, 3, 4, [1, 2, 3], 1, 10, 100]
a.remove(10)
print(a)#[1, 2, 15, 1, 1, 1, 1, 3, 4, [1, 2, 3], 1, 100]
a.pop(1)
print(a)#pop(1) 1 is index value [1, 15, 1, 1, 1, 1, 3, 4, [1, 2, 3], 1, 100]
a.reverse()
print(a)#[100, 1, [1, 2, 3], 4, 3, 1, 1, 1, 1, 15, 1]
b=a.copy()
print(b)#[100, 1, [1, 2, 3], 4, 3, 1, 1, 1, 1, 15, 1]
b.clear()
print(b)#[]
c=[1,2,0,4,5]
print(max(c))#5
print(min(c))#0
print(sorted(c))#[0,1,2,4,5]


