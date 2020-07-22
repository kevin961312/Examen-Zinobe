def kadane1D(array):
    sumMax = 0 , t=0
    ind= 0
    for j in range(len(array)):
        t+=array[j]
        if t>sumMax: 
            sumMax=t
            ini,finish=ind,j
        if t<=0:
            t=0
            ind=j+1
    return sumMax,ini,finish
