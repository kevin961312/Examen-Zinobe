def maximo_cuadrado(M):
    try:
        if set(chain.from_iterable(M)) == {1}:return (0,0,0)
        elif len(set(chain.from_iterable(M)))>2:
            return "La matriz posee números distintos de 1 y 0"
        elif len(set(chain.from_iterable(M))) ==0 : 
            return "La matriz no posee elementos"
        len_col,len_row=len(M[0]),len(M)
        if len_col >= len_row:
            date = list(kadane(M,len_row, len_col))
            width = abs(date[1]-date[3])+1
            length = abs(date[2]-date[4])+1
            return date[2],date[1],  min(length, width)
        else:
            date = list(kadane(M,len_col, len_row))
            width = abs(date[1]-date[3])+1
            length = abs(date[2]-date[4])+1
            return date[2],date[1], min(length, width)
    except ValueError:
        return "La matriz no cumple las condiciones"