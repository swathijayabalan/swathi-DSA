def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)  
    return result
coins = [1, 5, 10, 25]
amount = 63
solution = coin_change_greedy(coins, amount)
print(f"Coins used to make {amount}: {solution}")
