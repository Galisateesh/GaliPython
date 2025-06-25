class gali:
    def fact(self,n):
        if n==1 or n==0:
            return 1
        else:
            return n*self.fact(n-1)
    def fun(self,arr):
        ma=0
        for i in arr:
            if i>ma:
                ma=i
        return ma
    def perfect(self,p):
        t=0
        for i in range(1,p):
            if p%i==0:
                t=t+i
        if t==p:
            return "given number is perfect number"
        else:
            return "given number is not perfect number"
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
    def perfect1(self,k):
        t=0
        for i in range(1,k):
            if k%i==0:
                t=t+i
        if t==k:
            return k
    def arm1(self,p):
        n=p
        t=0
        while n>0:
            r=n%10
            t=t+r*r*r
            n=n//10
        if t==p:
            return p
    def neon1(self,n):
        k=n*n
        t=0
        while k>0:
            r=k%10
            t=t+r
            k=k//10
        if t==n:
            return n
g=gali()
op=int(input("enter your choice\n1.Factorial of given number\n2.Maximum of numbers\n3.Perfect number or Not\n4.Neon number or Not\n5.Armstrong number or Not\n6.Fibinacci series\n7.Perfect numbers range\n8.Armstrong number range\n9.Neon number range\n\n          "))
print(" ")
match op:
    case 1:
        n=int(input("enter number "))
        print(f"factorial of given number",g.fact(n))
    case 2:
        n=[]
        k=int(input("enter how many numbers"))
        print("enter those numbers")
        for i in range(k):
            i=int(input())
            n.append(i)
        o=g.fun(n)
        print("max value",o)
    case 3:
        o=int(input("enter number "))
        b=g.perfect(o)
        print(b,o)
    case 4:
        y=int(input("enter number "))
        print(g.neon(y),y)
    case 5:
        i=int(input("enter number "))
        print(g.arm(i),i)
    case 6:
        u=int(input("enter number "))
        print(' '.join(g.fibo(u-2)))
    case 7:
        o=int(input("enter start "))
        m=int(input("enter stop "))
        for i in range(o,m):
            if g.perfect1(i)!=None:
                print(g.perfect1(i))
    case 8:
        i=int(input("enter start "))
        j=int(input("enter stop "))
        for l in range(i,j+1):
            if g.arm1(l)!=None:
                print(g.arm1(l))
    case 9:
        y=int(input("enter start "))
        z=int(input("enter stop "))
        for i in range(y,z):
            if g.neon1(i)!=None:
                print(g.neon1(i))
    case _:
        print("please select valid choice")
        
    
    
