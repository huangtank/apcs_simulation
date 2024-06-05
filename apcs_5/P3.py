n, k, t = map(int, input().split())
a = [int(i) for i in input().split()]
l = 1
r = t//(n+1-k)
while l < r:
    x = l+r+1>>1
    last = 0
    cnt = 0
    for i in a:
        if i-last >= x:
            last = i
        else:
            cnt += 1
    if t-last < x:
        cnt += 1
    if cnt <= k:
        l = x
    else:
        r = x-1
print(l)