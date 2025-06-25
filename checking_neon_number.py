class gali:
    def neon(self,n):
        k=n*n
        t=0
        while k>0:
            r=k%10
            t=t+r
            k=k//10
        if t==n:
            return "given number is neon"
        else:
            return "given number is not neon"
g=gali()
y=int(input("enter number "))
print(g.neon(y),y)
            
