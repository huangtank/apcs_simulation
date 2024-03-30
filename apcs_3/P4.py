def count_combinations(volumes, total_volume, mod):
    m = len(volumes)
    dp = [[0] * (m + 1) for _ in range(total_volume + 1)]
    dp[0][0] = 1

    for i in range(1, total_volume + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= volumes[j - 1]:
                dp[i][j] += dp[i - volumes[j - 1]][j]
            dp[i][j] %= mod

    return dp[total_volume]

# 讀取輸入
n, m = map(int, input().split())  # n: 目標總體積, m: 酒的種類數量
volumes = list(map(int, input().split()))  # 酒的容量

# 計算可能的方案數
mod = 998244353
result = count_combinations(volumes, n, mod)

# 輸出結果，每個答案都取模 998244353
for r in result[1:]:
    print(r % mod, end=" ")
