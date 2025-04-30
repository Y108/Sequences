def seq_seq_index(A, B, bound=None):
    
    if not (isinstance(A, (list, str)) or isinstance(B, (list, str))) or (not isinstance(bound, int) and bound is not None):

        raise TypeError("Input has to be a list or string, and bound has to be an integer or None")

    elif bound == None:
        Zip = [[x,y] for x,y in zip(A,B)]
        S = {i:[] for i in list(sorted(set(A)))[::-1]}
        for k in range(len(Zip)):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            print(f"p({key}): {S[key]}")
    
    else:
        Zip = [[x,y] for x,y in zip(A,B)]
        S = {i:[] for i in list(set(A))[::-1]}
        for k in range(min(bound, len(Zip))):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            print(f"p({key}): {S[key]}")

def simple_seq_index(A, bound=None):
    
    if not isinstance(A, (list, str)) or (not isinstance(bound, int) and bound is not None):

        raise TypeError("Input has to be a list or string, and bound has to be an integer or None")

    elif bound == None:
        Zip = [[x,y] for x,y in zip(A,range(1,len(A)+1))]
        S = {i:[] for i in list(sorted(set(A)))[::-1]}
        for k in range(len(Zip)):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            print(f"p({key}): {S[key]}")
    
    else:
        Zip = [[x,y] for x,y in zip(A,range(1,len(A)+1))]
        S = {i:[] for i in list(set(A))[::-1]}
        for k in range(min(bound, len(Zip))):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            print(f"p({key}): {S[key]}")

def simple_seq_index_len(A, bound=None):
    
    if not isinstance(A, (list, str)) or (not isinstance(bound, int) and bound is not None):

        raise TypeError("Input has to be a list or string, and bound has to be an integer or None")

    elif bound == None:
        Zip = [[x,y] for x,y in zip(A,range(1,len(A)+1))]
        S = {i:[] for i in list(sorted(set(A)))[::-1]}
        for k in range(len(Zip)):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            print(f"p({key}): {len(S[key])}")
    
    else:
        Zip = [[x,y] for x,y in zip(A,range(1,len(A)+1))]
        S = {i:[] for i in list(set(A))[::-1]}
        for k in range(min(bound, len(Zip))):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            print(f"p({key}): {len(S[key])}")

def seq_index_len_list(A, bound=None):
    
    templ = []

    if not isinstance(A, (list, str)) or (not isinstance(bound, int) and bound is not None):

        raise TypeError("Input has to be a list or string, and bound has to be an integer or None")

    elif bound == None:
        Zip = [[x,y] for x,y in zip(A,range(1,len(A)+1))]
        S = {i:[] for i in list(sorted(set(A)))[::-1]}
        for k in range(len(Zip)):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            templ.append(len(S[key]))

        return templ
    
    else:
        Zip = [[x,y] for x,y in zip(A,range(1,len(A)+1))]
        S = {i:[] for i in list(set(A))[::-1]}
        for k in range(min(bound, len(Zip))):
            for j in S:
                if Zip[k][0] == j:
                    S[j].append(Zip[k][1])
        for key in S:
            templ.append(len(S[key]))

        return templ

def peak(A):
    return [A[i] for i in range(len(A)-1) if A[i] > A[i+1]]

def seq_index_peak(A, bound=None):
    if not isinstance(A, (list, str)) or (not isinstance(bound, int) and bound is not None):
        raise TypeError("Input has to be a list or string, and bound has to be an integer or None")

    Zip = [[x, y] for x, y in zip(A, range(1, len(A) + 1))]
    if bound is None:
        data = Zip
    else:
        data = Zip[:min(bound, len(Zip))]

    S_keys = list(sorted(set(A))) if bound is None else list(set(A))[::-1]
    S = {i: [] for i in S_keys}
    
    for x, y in data:
        if x in S:
            S[x].append(y)

    templ = [len(S[key]) for key in S_keys]

    return [S_keys[i] for i in range(len(templ) - 1) if templ[i] > templ[i + 1]]
