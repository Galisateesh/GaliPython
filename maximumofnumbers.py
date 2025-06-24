class gali:
    def fun(self,arr):
        ma=0
        for i in arr:
            if i>ma:
                ma=i
        return ma
n=[]
k=int(input("enter"))
for i in range(k):
    i=int(input())
    n.append(i)
c=gali()
o=c.fun(n)
print("max value",o)

        
