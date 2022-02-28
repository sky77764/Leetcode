# 10min - brute force (2299 ms, 14.2 MB)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    return [i, i+j+1]

        return None

# 10min - sort + brute force (3488 ms, 14.8 MB)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_idx = sorted(range(len(nums)), key=lambda k: nums[k])
        sorted_nums = []
        for i in range(len(nums)):
            sorted_nums.append(nums[sorted_idx[i]])

        for i, num1 in enumerate(sorted_nums):
            for j, num2 in enumerate(sorted_nums[i+1:]):
                if num1 + num2 == target:
                    return [sorted_idx[i], sorted_idx[i+j+1]]

        return None

# Solution - hash map (923 ms, 14.3 MB)
class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i

        for i, num in enumerate(nums):
            complement = target-num
            if complement in nums_dict.keys() and nums_dict[complement] != i:
                return [i, nums_dict[target-num]]
        return None

if __name__ == '__main__':
    test = Solution3()
    print(test.twoSum([2, 7, 11, 15], 9))
    print(test.twoSum([3, 2, 4], 6))
    print(test.twoSum([3, 3], 6))