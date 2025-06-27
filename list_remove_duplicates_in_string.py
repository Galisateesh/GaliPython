class gali:
    def dup(self,b):
        a=[]
        for i in b:
            if i not in a and i!=' ':
                a.append(i)
        return a
g=gali()
d=input("enter any\n")
c=g.dup(d)
print(c)#list format
print(' '.join(c))#string format

