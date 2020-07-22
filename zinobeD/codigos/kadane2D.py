def kadane(A,min_l,max_l):
    M = convert_matriz(A)
    sum_max = 0
    row_t ,col_t = 0,0
    row_f ,col_f = 0,0
    for g in range(min_l):
        sum_par = [0]*max_l
        for i in range(g, min_l):
            t=h=0
            for j in range(max_l):
                try:
                    sum_par[j]+= M[i][j]
                except IndexError:
                    continue
                    sum_par[j]+= M[j][i]   
                t+=sum_par[j]
                if t>sum_max:
                    sum_max = t 
                    row_t,col_t= h,g
                    row_f,col_f = j,i
                if t<=0:
                    t=0
                    h=j+1
    return sum_max,row_t,col_t,row_f,col_f