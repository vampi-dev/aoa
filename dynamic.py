def rod_cutting(price, n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], price[j-1] + dp[i-j])

    return dp[n]

price = [2, 5, 7, 8]
n = 4

print("Maximum profit:", rod_cutting(price, n))

def mcm(p, i, j):
    if i == j:
        return 0

    ans = float('inf')

    for k in range(i, j):
        cost = (mcm(p, i, k) +
                mcm(p, k+1, j) +
                p[i-1] * p[k] * p[j])
        ans = min(ans, cost)

    return ans

n = int(input("Enter number of matrices: "))
p = list(map(int, input("Enter dimensions: ").split()))
def lcs(a, b):
    m = len(a)
    n = len(b)

    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

a = input("Enter first string: ")
b = input("Enter second string: ")

print("LCS Length:", lcs(a, b))

print("Minimum cost:", mcm(p, 1, n))
