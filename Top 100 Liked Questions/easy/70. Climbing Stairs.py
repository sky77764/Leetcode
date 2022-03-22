# 6min, 20 ms	13.2 MB, O(n)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])

        return dp[n]


if __name__ == '__main__':
    sol = Solution()

    print(sol.climbStairs(2))