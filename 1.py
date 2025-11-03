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
print(permutations([1, 2, 3]))
print(permutations(['a', 'b']))

