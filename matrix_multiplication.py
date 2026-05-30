def input(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row by row:")
    matrix = []
    for i in range(rows):
        row = []
        print(f"Row {i+1}:")
        for j in range(cols):
            val = int(input(f"  Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix, rows, cols
def multiply(A, B, r1, c1, r2, c2):
    if c1 != r2:
        print("Matrix multiplication not possible")
        return None
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result
A, r1, c1 = input("Matrix A")
B, r2, c2 = input("Matrix B")
product = multiply(A, B, r1, c1, r2, c2)
if product:
    print("Resultant Matrix:")
    for row in product:
        for val in row:
            print(val, end=" ")
        print()

