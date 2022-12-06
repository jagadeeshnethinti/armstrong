a=int(input())
r=0
m=a
while(a!=0):
    rem=a%10
    r=r+rem*rem*rem
    a=a//10
if(r==m):
    print('armstrong')
else:
    print('not a armstrong')