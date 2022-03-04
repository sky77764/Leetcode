# sol, 644 ms	25.5 MB, O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        max = dp[0]

        for i in range(1, len(nums)):
            dp.append(dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i])
            max = max if max > dp[i] else dp[i]

        return max


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1]
    nums = [5, 4, -1, 7, 8]
    nums = [8, -19, 5, -4, 20]
    print(sol.maxSubArray(nums))