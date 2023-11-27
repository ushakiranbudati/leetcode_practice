from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy_price = prices[0]
        sell_price = 0

        for i in range(1, len(prices)):
            current_profit = prices[i] - buy_price

            # Update buy_price if a lower price is encountered
            if prices[i] < buy_price:
                buy_price = prices[i]

            # Update sell_price if a higher profit is encountered
            if current_profit > sell_price:
                sell_price = current_profit

        return sell_price
prices = [1,2,4]
sol = Solution()
output = sol.maxProfit(prices)
print(output)