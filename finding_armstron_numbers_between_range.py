class gali:
    def arm(self,p):
        n=p
        t=0
        while n>0:
            r=n%10
            t=t+r*r*r
            n=n//10
        if t==p:
            return p
d=gali()
i=int(input("enter start "))
j=int(input("enter stop "))
for l in range(i,j+1):
    if d.arm(l)!=None:
        print(d.arm(l))
