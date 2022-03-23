# sol, 120 ms	14.2 MB
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        max_len = 0
        cur_idx = 0

        for i in range(len(s)):
            if s[i] in dict.keys() and cur_idx <= dict[s[i]]:
                cur_idx = dict[s[i]] + 1
            else:
                max_len = max(max_len, i - cur_idx + 1)
            dict[s[i]] = i
        return max_len



if __name__ == '__main__':
    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    # s = " "
    # s = "abba"
    # s = "dvdf"
    # s = "tmmzuxt"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
