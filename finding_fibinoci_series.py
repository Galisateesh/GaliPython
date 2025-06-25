class gali:
    def fibo(self,c):
        s=0
        p=1
        o=['0','1']
        while c>0:
            t=s+p
            s=p
            p=t
            o.append(str(t))
            c=c-1
        return o
g=gali()
u=int(input("enter number "))
print(' '.join(g.fibo(u-2)))
