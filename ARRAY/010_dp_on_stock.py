#The core idea of this solution is to **track the minimum price seen so far** while iterating through the stock prices and, at each step, calculate the profit if we were to sell at the current price. By updating the maximum profit found and the minimum price along the way, we ensure that we’re always considering the best possible **buy low, sell high** scenario in a single pass, making the solution efficient with `O(n)` time and `O(1)` space complexity.

def buy_sell_sotck(nums):
    mini=nums[0]
    n=len(nums)
    profit=0
    for i in range(1,n):
        curr_profit=nums[i]-mini
        profit=max(profit,curr_profit)
        mini =min(mini, nums[i])
    return profit