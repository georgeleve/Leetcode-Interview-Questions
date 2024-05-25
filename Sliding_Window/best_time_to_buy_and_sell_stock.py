# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://www.youtube.com/watch?v=1pkOgXD63yU&t=393s
# Questions to ask the interviewer
# Is this array sorted?
# Can we expect an empty array?
# Does the array include only positive integers?

class Solution(object):
    '''
    # One pass solution. O(n) Time Complexity | O(1) Space Complexity
    # where n is the number of elements in the array
    def maxProfit(self, prices):
        minPrice = float("inf")
        maxProfit = 0
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif (prices[i] - minPrice) > maxProfit:
                maxProfit = (prices[i]- minPrice)
        return maxProfit
    '''
    #One pass using two pointers approach | O(n) Time Complexity (linear time complexity) | O(1) Space Complexity were n is the number of elements in the input array
    def maxProfit(self, prices):
        left = 0 # Buy stock #we ant the left poiinter to be the minimum
        right = 1 # Sell stock
        maxProfit = 0
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                currentProfit = prices[right] - prices[left]
                maxProfit = max(currentProfit, maxProfit)
            right += 1
        return maxProfit



    '''
    # brute force solution. O(n) Time Complexity | O(1) Space Complexity
    # Throws a time limit exceeded error
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
     '''