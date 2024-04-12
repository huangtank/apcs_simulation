n, m = map(int, input().split())
S = []
for _ in range(4):
    S.append([int(i) for i in input().split()])
a = [int(i) for i in input().split()]
ans = []
for i in a:
    temp = bin(i)[2::]
    if len(temp)-n<0:
        temp = '0'*(n-len(temp))+temp
    b = temp[0]+temp[-1]
    temp = temp[1:-1]
    if b == '00':
        ans.append(S[0][int(temp, 2)])
    elif b == '01':
        ans.append(S[1][int(temp, 2)])
    elif b == '10':
        ans.append(S[2][int(temp, 2)])
    else:
        ans.append(S[3][int(temp, 2)])
print(*ans)