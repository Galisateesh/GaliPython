n=5
for i in range(n):
    for j in range(n):
        if i>0 and j>0 and i<4 and j<4:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
