import sys
sys.setrecursionlimit(1000000)
n = int(input())
con = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int,input().split())
    con[u-1].append(v-1)
    con[v-1].append(u-1)
a = [int(i) for i in input().split()]
def dfs(i,p):
    s1 = 0
    s2 = 0
    s3 = 10**10
    for j in con[i]:
        if j != p:
            o = dfs(j, i)
            s1 += o[2]
            s2 += o[1]
            s3 = min(s3, o[0]-o[1])
    ret = [s1+a[i], s2+s3,s2]
    ret[1] = min(ret[1], ret[0])
    ret[2] = min(ret[2], ret[1])
    return ret
print(dfs(0, -1)[1])