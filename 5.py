def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []
    # Total combinations = 2^n
    for i in range(2 ** n):
        combo = bin(i)[2:].zfill(n)  
        total_weight = 0
        total_value = 0
        items_included = []
        for j in range(n):
            if combo[j] == '1':
                total_weight += weights[j]
                total_value += values[j]
                items_included.append(j)
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = items_included
    return max_value, best_combination
weights = [1,2,3,4,6,7]
values =  [4,5,9,8,12,7]
capacity = 16
max_val, items = knapsack_brute_force(weights, values, capacity)
print("Maximum Value:", max_val)
print("Items Included:", items)

