class gali:
    def perfect(self,p):
        t=0
        for i in range(1,p):
            if p%i==0:
                t=t+i
        if t==p:
            return "given number is perfect number"
        else:
            return "given number is not perfect number"
                
g=gali()
o=int(input("enter number "))
print(g.perfect(o),o)

