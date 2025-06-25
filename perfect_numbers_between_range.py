class gali:
    def perfect(self,k):
        t=0
        for i in range(1,k):
            if k%i==0:
                t=t+i
        if t==k:
            return k
            
                
g=gali()
o=int(input("enter start "))
m=int(input("enter stop "))
for i in range(o,m):
    if g.perfect(i)!=None:
        print(g.perfect(i))


