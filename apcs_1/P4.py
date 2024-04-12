from heapq import heappush, heappop

#拓樸排序，結果為result
pq = []
result = []
def topo_sort():
    for i in range(1, n+1): #先提出沒有要求的點
        if degree[i] == 0:
            heappush(pq, i)
    while len(pq) > 0:
        c = heappop(pq)
        result.append(c)
        for child in d[c]:
            degree[child] -= 1
            if degree[child] == 0:
                heappush(pq, child)

n = int(input())
degree = [0]*(n+1)
d = [[] for _ in range(n+1)]
#建圖
for i in range(1, n+1):
    a = [int(i) for i in input().split()]
    k = a[0]
    for j in range(1, len(a)):
        d[a[j]].append(i)
        degree[i] += 1
topo_sort()
print(*result)