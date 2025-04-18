def seq_seq_index(A, B): 
        
        X = len(A)
        Y = len(B)

        abs_diff = abs(Y - X)

        def main(A,B):

            S = {i:[] for i in list(set(A))[::-1]}
            for k in range(Y):
                for i in set(A):
                    if A[k] == i:
                        S[i].append(B[k])
            for key in S:
                print(f"p({key}): {S[key]}")

        if not(isinstance(A, list) and isinstance(B, list)):
                
            raise ValueError("Both inputs of function have to be of type list!")
        
        elif not(X > 0 and Y > 0):
                
            raise ValueError("Both inputs of function have to contain at least one element!")

        elif any(isinstance(item, str) and item.strip() == "" for item in A or B):

            raise ValueError("Both inputs of function can't contain any empty elements (e.G. " " or ' ')")
        
        elif sorted(list(set(A))) == sorted(A):
                
                if X == Y:
                    print(f'I:{A}\nII:{B}')
                
                if X > Y:
                    print(f'I:{A[:-abs_diff]}\nII:{B}')

                if X < Y:
                    print(f'I:{A}\nII:{B[:-abs_diff]}')

        else:
                if X>=Y:
                    main(A,B)

                elif X<Y:
                    B2 = B[:-abs_diff]
                    main(A,B2)

                else:
                    return None

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
