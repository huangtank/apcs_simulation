#差分
n, m = map(int,input().split())
s = input()
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
o = {"W":0, "M":1, "L":2} #b的位置
c = [0]*n #時間圖
for i, ch in enumerate(s):
    j = o[ch]
    c[i] += a[j]
    p = i+b[j]
    if p<n: #判斷會不會超出串列長度
        c[p] -= a[j]
ans = 0
cur = 0
for i in c:
    cur += i
    ans += cur>m
print(ans)