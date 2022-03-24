# check again
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                left = s[i] + self.longestPalindrome(s[dict[s[i]] + 1:i]) + s[i]
                right = self.longestPalindrome(s[i:])
                if left == right:
                    return left+right[1:]
                return left if len(left) >= len(right) else right
        return s[0]


if __name__ == '__main__':
    s = "babad"
    s = "cbbd"
    # s = "ac"
    s = "ccc"
    s = "aaaa"

    sol = Solution()
    print(sol.longestPalindrome(s))