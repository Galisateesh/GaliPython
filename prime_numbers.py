class gali:
    def prime(self):
        f=[]
        for n in range(2,100):
            c=0
            for i in range(1,n+1):
                if n%i==0:
                    c+=1
            if c==2:
                f.append(str(n))
        return f
k=gali()
g=k.prime()
p=','.join(g)
print(p)
