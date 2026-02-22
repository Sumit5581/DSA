class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = list(range(len(w2) + 1))

        for i in range(1, len(w1) + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, len(w2) + 1):
                cur = dp[j]
                if w1[i - 1] == w2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                prev = cur

        return dp[-1]