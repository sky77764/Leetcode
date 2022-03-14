# 8min, 	239 ms	14.7 MB
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1

            if dict[num] > len(nums) / 2:
                return num


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majorityElement(nums))