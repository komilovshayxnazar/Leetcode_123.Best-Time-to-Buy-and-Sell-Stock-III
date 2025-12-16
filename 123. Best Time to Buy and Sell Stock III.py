class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)

        first_transaction = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            first_transaction[i] = max(first_transaction[i - 1], prices[i] - min_price)

        max_profit = 0
        max_price = prices[-1]
        second_transaction = 0

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            second_transaction = max(second_transaction, max_price - prices[i])
            max_profit = max(max_profit, first_transaction[i] + second_transaction)

        return max_profit