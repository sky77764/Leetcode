# 10min, 66 ms	13.7 MB
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_bracket = ['(', '[', '{']
        close_bracket = [')', ']', '}']
        bracket_dict = {')': '(', ']': '[', '}': '{'}

        stack = []
        for char in s:
            if char in open_bracket:
                stack.append(char)
            elif char in close_bracket:
                if len(stack) == 0:
                    return False

                if stack[-1] == bracket_dict[char]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True


if __name__ == '__main__':
    sol = Solution()
    s1 = "]"
    s2 = "()[]{}"
    s3 = "(]"
    print(sol.isValid(s1))
    print(sol.isValid(s2))
    print(sol.isValid(s3))