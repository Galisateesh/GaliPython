class gali:
    def arm(self,p):
        n=p
        t=0
        while n>0:
            r=n%10
            t=t+r*r*r
            n=n//10
        if t==p:
            return "this is arm strong number"
        else:
            return "this is not armstrong number"
d=gali()
i=int(input("enter number "))
print(d.arm(i),i)
