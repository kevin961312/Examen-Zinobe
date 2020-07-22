element = lambda M,row,col: [M[i][j] for i in range(row-1,row+2) for j in range(col-1,col+2)
                            if (0 <= i < len(M) and 0 <= j < len(M[0]))]
neigh   = lambda M,row,col: {(i,j) for i in range(row-1,row+2) for j in range(col-1,col+2)
                            if (0 <= i < len(M) and 0 <= j < len(M[0]))}