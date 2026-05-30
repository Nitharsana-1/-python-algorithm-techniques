def permutations(arr):
    result = []
    def backtrack(s):
        if s == len(arr):
            result.append(arr[:])  
            return
        for i in range(s, len(arr)):
            arr[s], arr[i] = arr[i], arr[s]  
            backtrack(s + 1)
            arr[s], arr[i] = arr[i], arr[s] 
    backtrack(0)
    return result
def tsp_brute_force(dist_matrix, source=0):
    n = len(dist_matrix)
    cities = []
    for i in range(n):
        if i != source:
            cities.append(i)
    all_routes = permutations(cities)
    min_distance = float('inf')
    best_path = []
    for route in all_routes:
        path = [source]+route+[source]
        total = 0
        for i in range(len(path) - 1):
            total += dist_matrix[path[i]][path[i+1]]
        if total<min_distance:
            min_distance = total
            best_path = path
    return min_distance, best_path
dist_matrix = [
    [0,10,20,32,25],
    [10,0,33,25,31],
    [15,34,35,0,21],
    [20,25,30,0,15],
    [25,30,20,15,0]
]
min_dist, route = tsp_brute_force(dist_matrix)
print("Minimum Distance:", min_dist)
print("Optimal Route:", route)

