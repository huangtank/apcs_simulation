n,p,m,k,d=map(int,input().split())
no=p-n-k
have=n-m
if have+no+d>=n:
    print('Sad :((')
    print((have-n)+no+d-1)
else:
    print('Happy :>')
    print(n-(have+no+d))