c1, c2, v1, v2 = map(int, input().split())
if c1*v1*2 == c2*v2*5:
    print('Yes')
    print(c1*v1*2)
else:
    print('NO')