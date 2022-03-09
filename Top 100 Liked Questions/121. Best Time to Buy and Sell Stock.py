# 10min, 1085 ms	22.9 MB
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        min_val = 100000
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]

            cur_profit = prices[i] - min_val
            if cur_profit > max_profit:
                max_profit = cur_profit

        return max_profit



if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]

    sol = Solution()
    print(sol.maxProfit(prices))