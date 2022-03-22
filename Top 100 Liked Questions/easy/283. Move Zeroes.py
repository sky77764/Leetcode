# 10 min, 6430 ms	14.6 MB
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i, num in enumerate(nums):
            if num == 0 and len(nums[i:]) > 1:
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
        return nums




if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums = [0]
    sol = Solution()
    print(sol.moveZeroes(nums))