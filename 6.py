def combinations(arr):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
def knapsack(weights, values, capacity):
    n = len(weights)
    items = list(range(n))  
    all_combos = combinations(items)
    max_value = 0
    best_combo = []
    for combo in all_combos:
        total_weight = sum(weights[i] for i in combo)
        total_value = sum(values[i] for i in combo)
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combo = combo
    return max_value, best_combo
weights = [1,2,3,4,6,7]
values =  [4,5,9,8,12,7]
capacity = 16
max_val, items = knapsack(weights, values, capacity)
print("Maximum Value:", max_val)
print("Items Included:", items)
