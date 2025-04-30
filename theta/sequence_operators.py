def seq_add(A, B):
    return [a + b for a, b in zip(A, B)]

def seq_diff(A, B):
    return [a - b for a, b in zip(A, B)]

def seq_self_diff(A):
    return [(A[i + 1] - A[i]) for i in range(len(A) - 1)]

def seq_mod_n(A, n):
    return [a % n for a in A]

def seq_mod_seq(A, B):
    return [a % b for a, b in zip(A, B)]

def seq_mult(A, B):
    return [a*b for a, b in zip(A, B)]

def seq_div(A, B):
    return [a/b for a, b in zip(A, B)]

def seq_div_floor(A, B):
    return [a//b for a,b in zip(A, B)]

def seq_div_ceil(A, B):
    def div_ceil(x, y):
        return -(x // -y)
    return [div_ceil(a,b) for a,b in zip(A,B)]

def seq_power(A, B):
    return [a**b for a,b in zip(A, B)]

def seq_root(A,B):
    return [a**(1/float(b)) for a,b in zip(A,B)]

def seq_powroot(A, B, C):
    return [a**(float(c)/float(b)) for a,b,c in zip(A,B,C)]
