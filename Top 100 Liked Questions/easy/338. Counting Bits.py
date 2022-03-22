# 20 min, 74 ms	17.3 MB
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out = []
        j = 1
        idx = 0
        for i in range(n+1):
            if i < 2:
                out.append(i)
            else:
                if i >= 2 ** j:
                    j += 1
                    idx = 0
                out.append(out[idx] + 1)
                idx += 1
        return out


if __name__ == '__main__':
    sol = Solution()
    n = 5
    print(sol.countBits(n))