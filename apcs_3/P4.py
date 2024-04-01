mod = 998244353
n, m = map(int, input().split())
wine = [int(i) for i in input().split()]
dp = [1]+[0]*(n)
dp0 = [0]*(n+2)
for i in range(n+1):
    dp0[i+1] = dp[i] + dp0[i]
for x in wine:
    for j in range(n, -1, -1):
        dp[j] = (dp0[j+1] - dp0[max(0, j-x)]) % mod
    for i in range(n+1):
        dp0[i+1] = dp[i] + dp0[i]
print(*dp[1::])