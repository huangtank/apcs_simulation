t = int(input())
count = [0, 0] #分數
N = [0, 0] #單子數
for _ in range(t):
    p, n = [int(i) for i in input().split()]
    if p > n:
        N[0] += 1
    else:
        N[1] += 1
    count[0] += p
    count[1] += n
flag = True #正為正方獲勝，否為反方獲勝
if N[0] != N[1]:
    if N[0] < N[1]:
        flag = False
else:
    if count[0] < count[1]:
        flag = False
if flag:
    print("Positive side")
else:
    print("Negative side")
print(*N)
print(*count)


#100分