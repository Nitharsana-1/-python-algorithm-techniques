def combinations(arr, r):
    result = []
    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])  
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)  
            path.pop()  

    backtrack(0, [])
    return result
print(combinations([1, 2, 3], 2))
print(combinations(['a', 'b', 'c', 'd'], 3))


