n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    for l in range(i):
        print('*',end=' ')
    print()
for i in range(n-1):
    for j in range(i+2):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('*',end=' ')
    for k in range(i,n-2):
        print('*',end=' ')
    print()
print("\n\n         OR\n\n")
for i in range(n):
    for k in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*  ',end=' ')
    print()
for i in range(n-1):
    for k in range(i+2):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*  ',end=' ')
    print()

