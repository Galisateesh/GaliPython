class gali:
    def fact(self,n):
        if n==1 or n==0:
            return 1
        else:
            return n*self.fact(n-1)
d=gali()
n=int(input("enter number "))
print(f"factorial of given number {d.fact(n)}")
        
