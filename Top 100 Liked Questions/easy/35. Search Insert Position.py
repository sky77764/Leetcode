# 20min, 55 ms	14.3 MB
class Solution(object):
    def quicksearch(self, nums, target, init_idx):
        center_idx = int(len(nums) / 2)
        if nums[center_idx] == target:
            return center_idx + init_idx
        elif nums[center_idx] < target:
            if len(nums[center_idx:]) == 1:
                return center_idx + init_idx + 1
            else:
                return self.quicksearch(nums[center_idx + 1:], target, center_idx + init_idx + 1)
        else:
            if len(nums[:center_idx]) == 0:
                return center_idx + init_idx
            else:
                return self.quicksearch(nums[:center_idx], target, init_idx)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.quicksearch(nums, target, init_idx=0)

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(sol.searchInsert(nums, target))