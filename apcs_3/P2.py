def find(x, y, r, c, R):
    idx = arr[x][y]
    temp = 0
    for x1,y1 in (x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1):
        if x1 < 0 or y1 < 0 or x1 >= r or y1 >= c:
            continue
        for x2,y2 in (x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1):
            if x2 < 0 or y2 < 0 or x2 >= r or y2 >= c:
                continue
            elif x1 == x2 and y1 == y2:
                continue
            if (arr[x1][y1] + arr[x2][y2]) % R == idx:
                temp += 1
    tone[x][y] = temp >> 1

def find_xy(x, y, r, c):
    ans = 0
    idx = tone[x][y]
    for i,j in (x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1):
        if i < 0 or j < 0 or i >= r or j >= c:
            continue
        if tone[i][j] == idx:
            ans += 1
    return ans
n, m, R = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])

tone = [[0]*(m) for _ in range(n)]
for i in range(n):
    for j in range(m):
        find(i, j, n, m, R)

ans = 0
for i in range(n):
    for j in range(m):
        ans += find_xy(i, j, n, m)
print(ans >> 1)