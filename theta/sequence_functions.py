def seq_assign(A, B): 
        
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

        def errors(n):  

            if n == 1: print('\033[91mWarning: Both inputs of \033[93madd_lst\033[91m have to be of type list!\033[0m')
            if n == 2: print('\033[91mWarning: Both inputs of \033[93madd_lst\033[91m have to contain at least \033[93m 1 \033[91m element!\033[0m')

        if sorted(list(set(A))) == sorted(A): #check if the output equals the 1-1 assignment of the two sequences
            

            if X == Y:
                print(f'I:{A}\nII:{B}')
            
            if X > Y:
                print(f'I:{A[:-abs_diff]}\nII:{B}')

            if X < Y:
                print(f'I:{A}\nII:{B[:-abs_diff]}')
        
        elif not(isinstance(A, list) and isinstance(B, list)):
            errors(2)
        
        elif not(X > 0 and Y > 0):
            errors(2)

        else:
                if X>=Y:
                    main(A,B)

                elif X<Y:
                    B2 = B[:-abs_diff]
                    main(A,B2)

                else:
                    return None
