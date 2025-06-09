# Best Time to Buy and Sell Stock Easy Topics premium lock icon Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock. Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: list[int]):
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if min_price > price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == '__main__':
    sol = Solution()
    profit = sol.maxProfit([7, 1, 5, 3, 6, 4])
    print(profit)