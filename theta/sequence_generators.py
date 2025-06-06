def FracDel(n):
    A = [3]
    def sub(A, j):
        B = [x for x in A for y in range(2)]
        i = 0
        C = [(7 + (i := i + B[k])) % 4 for k in range(2**(j+1)-2)]
        return [3] + C
    for j in range(n):
        A = sub(A, j)
    return A

def Collatz(n):
    S = [n]

    if n == 0:
        return []
    
    while n != 1:
        if n%2 == 0:
            n = n//2
        else:
            n= 3*n+1
        S.append(n)
    return S

def II_ThueMorse(n):
    a, b = '0', '1'
    for j in range(n):
        a, b = a + b, b + a
    return [*(int(x) for x in a)]

def III_ThueMorse(n):
    K = [3]
    for j in range(n):
        K = [int(i) for i in ''.join(
            str(32) if x == 3 else 
            str(13) if x == 2 else 
            str(12) if x == 1 else 
            str(x) for x in K)]
    return K

def IV_Thue_Morse(n):
    K = [4]
    for j in range(n):
        K = [int(i) for i in ''.join(
            str(4123) if x == 4 else 
            str(3412) if x == 3 else 
            str(2341) if x == 2 else 
            str(1234) if x == 1 else 
            str(x) for x in K)]
    return K

def Index(n):
    return list(range(1, n+1))

def Fibonacci(n):
    F = [1,]
    a,b = 0,1
    for i in range(n):
        c = a + b
        F.append(c)
        a = b
        b = c
    return F
