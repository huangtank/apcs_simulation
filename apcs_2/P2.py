n, q = map(int, input().split())
player = []
player.append([0]+[int(i) for i in input().split()])

#建立
for i in range(n):
    m, s, down, up = map(int, input().split())
    temp = player[-1][1::].copy()
    node = temp.index(down)
    temp[node] = up
    player.append([m*60+s]+temp)

#詢問
for _ in range(q):
    m, s = map(int, input().split())
    m = m*60+s
    for i in range(1,n+1):
        if  m < player[i][0]:
            print(*player[i-1][1::])
            break
    else:
        print(*player[-1][1::])