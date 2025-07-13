def knapsack(i, remaining_weight, weights, profits):
    if i < 0 or remaining_weight <= 0:
        return 0

    if weights[i] > remaining_weight:
        # Can't take the item
        return knapsack(i - 1, remaining_weight, weights, profits)
    else:
        # Take the item
        take = profits[i] + knapsack(i - 1, remaining_weight - weights[i], weights, profits)
        # Don't take the item
        not_take = knapsack(i - 1, remaining_weight, weights, profits)
        return max(take, not_take)
weights = [1, 3, 4, 5]
profits = [1, 4, 5, 7]
capacity = 7
n = len(weights)

print(knapsack(n - 1, capacity, weights, profits))
