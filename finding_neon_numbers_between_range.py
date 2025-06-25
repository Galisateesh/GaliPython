class gali:
    def neon(self,n):
        k=n*n
        t=0
        while k>0:
            r=k%10
            t=t+r
            k=k//10
        if t==n:
            return n
g=gali()
y=int(input("enter start"))
z=int(input("enter stop"))
for i in range(y,z):
    if g.neon(i)!=None:
        print(g.neon(i))
