N,M,n,q = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(N)]
l = [list(map(int, input().split())) for _ in range(n)]
for a in range(N):
    for b in range(M):
        for w in range(1, 51):
            for x,y,m in l:
                cal = w-abs(a-x)-abs(b-y)+h[x][y]
                cal = min(max(0, cal), 50)
                if cal != m:
                    break
            else:
                for _ in range(q):
                    x, y = map(int, input().split())
                    cal = w-abs(a-x)-abs(b-y)+h[x][y]
                    cal = min(max(0, cal), 50)
                    print(cal)
                break
        else:
            continue
        break
    else:
        continue
    break