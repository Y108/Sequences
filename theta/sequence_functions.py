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
