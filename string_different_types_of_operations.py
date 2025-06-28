class gali:
    l=['a','e','i','o','u']
    def vowels(self,a):
        c=[]
        for i in a:
            if i in self.l:
                c.append(i)
        return c
    def dup(self,b):
        li=[]
        for i in b:
            if i not in li:
                li.append(i)
        return li
    def consonants(self,a):
        c=[]
        for i in a:
            if i not in self.l:
                if i!=' ':
                    c.append(i)
        return c
    def shortcut(self,a):
        c=a[0]
        for i in range(len(a)):
            if a[i]==' ':
                c=c+a[i+1]
        return c
    def replac(self,a):
        k=''
        for i in range(len(a)):
            if a[i] in self.l:
                k=k+'*'
            else:
                k=k+'#'
        return k
    def after(self,a):
        k=''
        for i in range(len(a)):
            if a[i]!=' ':
                t=ord(a[i])
                k=k+chr(t+1)
        return k
    def Eveodd(self,a):
        e=''
        o=''
        for i in range(len(a)):
            if i%2==0 and a[i]!=' ':
                e=e+a[i]
            elif i%2==1 and a[i]!=' ':
                o=o+a[i]
        return e,o
    def fin(self,a,k):
        s=a
        p=k
        for i in range(len(s)):
            if s[i]==p:
                c=i
                break
        return c
                
a=int(input("Select Your Choice\n1.Find Vowels In A String\n2.Find Consonants In A String\n3.shortcut Name\n4.Vowels Replace With \'*' And Consonants with \'#'\n5.After Letters\n6.Even Place Letters And Odd Place Letters\n7.Finding Index Of Key\n"))
g=gali()
match a:
    case 1:
        k=input("enter string\n")
        t=g.vowels(k)
        for i in g.dup(t):
            x=t.count(i)
            print(i,x)
    case 2:
        k=input("enter string\n")
        t=g.consonants(k)
        for i in g.dup(t):
            x=t.count(i)
            print(i,x)
    case 3:
        k=input("enter string\n")
        print(g.shortcut(k))
    case 4:
        k=input("enter string\n")
        print(g.replac(k))
    case 5:
        k=input("enter string\n")
        print(g.after(k))
    case 6:
        k=input("enter string\n")
        c,d=g.Eveodd(k)
        print(f"Even Place Letters={c}\nOdd Place Letters={d}")
    case 7:
        t=input("enter string\n")
        o=input("enter key you want to find\n")
        d=g.fin(t,o)
        print(f"The Key='{o}' Found At Index='{d}'")
    case _:
        print("Please Select Right Choice Between 1-7")
        
