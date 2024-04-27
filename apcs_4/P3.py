n, m = map(int, input().split())
arr = input()
happy = [int(i) for i in input().split()] # W M L 開心度
time = [int(i) for i in input().split()] # W M L 時間

ans = 0
happy_mon = [0, 0, 0]
happy_time = [0, 0, 0]
for i in arr:
    for idx in range(3):
        if not(happy_time[idx]):
            happy_mon[idx] = 0
    if i == 'W':
        happy_mon[0] += happy[0]
        happy_time[0] += time[0]
    elif i == 'M':
        happy_mon[1] += happy[1]
        happy_time[1] += time[1]
    else:
        happy_mon[2] += happy[2]
        happy_time[2] += time[2]
    if sum(happy_mon) > m:
        ans += 1
    happy_time = [i-1 for i in happy_time]
print(ans)

# 85分