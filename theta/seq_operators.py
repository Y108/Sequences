def seq_assign(A, B): 
        def errors(n):  
            if n == 1: print('\033[91mWarning: Both inputs of \033[93madd_lst\033[91m have to be of type list!\033[0m')
            if n == 2: print('\033[91mWarning: Both inputs of \033[93madd_lst\033[91m have to contain at least \033[93m 1 \033[91m element!\033[0m')
            if n == 3: print('\033[91mWarning: The \033[93msecond\033[91m list has to be \033[93msmaller\033[91m than the \033[93mfirst\033[91m!\033[0m')
        if isinstance(A, list) and isinstance(B, list):
            if len(A) > 0 and len(B) > 0:
                if len(A)>=len(B):
                    S = {i:[] for i in list(set(A))[::-1]}
                    for k in range(len(B)):
                        for i in set(A):
                            if A[k] == i:
                                S[i].append(B[k])
                    for key in S:
                        print(f"p({key}): {S[key]}")
                else:
                    errors(3)
            else:
                errors(2)
        else:
            errors(1)
