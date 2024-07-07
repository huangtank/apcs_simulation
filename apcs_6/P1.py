n, m = map(int, input().split())
age = [int(i) for i in input().split()]
yo = []
for _ in range(int(input())):
    yo.append([int(i) for i in input().split()])
ans = 0
for person in age:
    for L, R, P in yo:
        if L <= person <= R:
            ans += P
            break
    else:
        ans += m
print(ans)