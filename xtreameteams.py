T= int(input())
for i in range(T):
    list=[]
    N,M =input().split(' ')
    N=int(N)
    M=int(M)
    for c in range(N):
        yes_no=input("y or n")
        list.append(yes_no)
    y = 0
    x = 0
    yes_c=0
    for co in range(M):
     while x <= N+1:
         if 'n' in list[x][y]:
             x=x+1
         else:
             yes_c+=1
             x+=1
    x=0
    y+=1
    if yes_c==0:
        print('o')
    else:
        print("ok")
