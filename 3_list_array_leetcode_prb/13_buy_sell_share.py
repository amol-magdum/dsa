# buy and sell shares to maximize profit
#brutful solution
def maxProfit(prices):
    n = len(prices)
    profit = 0
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] > prices[i]:
                h = prices[j] - prices[i]
                profit = max(profit, h)
    return profit
# test cases
arr1 = [7,1,5,3,6,4]
arr2 = [1,2,3,4,5]
print(maxProfit(arr1)) # 7
print(maxProfit(arr2)) # 4
#time complexity: O(n^2)
#space complexity: O(1)

#optimal solution
def maxProfitOptimal(prices):
    n = len(prices)
    min_price = float('inf')
    max_profit = 0

    for i in range(n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

# test cases
arr1 = [7,1,5,3,6,4]
arr2 = [1,2,3,4,5]
print(maxProfitOptimal(arr1)) # 7
print(maxProfitOptimal(arr2)) # 4
#time complexity: O(n)
#space complexity: O(1)