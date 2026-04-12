
def find_min_coin(coins, k):
    result =[]
    n = len(coins)

    for i in range(n-1, -1,-1):
        while k >=coins[i]:
            result.append(coins[i])
            k-=coins[i]
    return result

coins = [1,2,5,10,20,50,100,200,500,2000]
print(find_min_coin(coins,77))