
# 7min, 2021 ms	16.6 MB
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num in dict.keys():
                del dict[num]
            else:
                dict[num] = 1

        return list(dict.keys())[0]



if __name__ == '__main__':
    nums = [2, 2, 1]
    # nums = [4, 1, 2, 1, 2]

    sol = Solution()
    print(sol.singleNumber(nums))