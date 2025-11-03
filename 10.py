def karatsuba(x, y):
    print("The Value for Karatsuba Algorithm is" , x," ,",y)
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    print("The order of split", m)
    A, B = divmod(x, 10**m)
    C, D = divmod(y, 10**m)
    print("The  Value " ,x," is split into ", A , "and " ,B, " using division n modulo")
    print("The  Value " ,y," split into ", C , "and " ,D, " using division n modulo")
    AC = karatsuba(A, C)                  
    print("The AC Value is ", AC)
    BD = karatsuba(B, D)                   
    print("The BD Value is ", BD)
    ADpBC = karatsuba(A + B, C + D) - AC - BD  
    print("The AD+BC Value is ", ADpBC)
    result= AC * (10**(2*m)) + ADpBC * (10**m) + BD
    print("Result: ",result)
    return result
def test_karatsuba():
    x, y = 12345, 6789
    result = karatsuba(x, y)
    print(f"{x} × {y} = {result}")
    print(f"Verification: {x * y == result}")
test_karatsuba()
