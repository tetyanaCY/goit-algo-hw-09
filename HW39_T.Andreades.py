def find_coins_greedy(amount, coins):
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
            if amount == 0:
                break
    return result

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins to make up 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                amount -= coin
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                break
    return result

# Test the functions with an amount of 113 and coins [50, 25, 10, 5, 2, 1]
amount = 113
coins = [50, 25, 10, 5, 2, 1]

greedy_result = find_coins_greedy(amount, coins)
dynamic_result = find_min_coins(amount, coins)

greedy_result, dynamic_result
