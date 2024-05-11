#DSU(併查集)
def g(i): #找老大
    if dsu[i] == -1: return i
    dsu[i] = g(dsu[i])
    return dsu[i]

def m(a, b): #合併老大
    a = g(a)
    b = g(b)
    if a != b:
        dsu[a] = b
    return a != b
n, m = [int(i) for i in input().split()]
lines = [[int(i) for i in input().split()] for _ in range(m)]
k = int(input())
lines.sort(key=lambda x:x[2])
cur = n
dsu = [-1 for _ in range(n)]
for a, b, c in lines:
    cur -= m(a,b)
    if cur < k:
        print(c)
        break