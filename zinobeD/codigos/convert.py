def convert_matriz(A):
    A = np.array(A, dtype=np.float)
    A = np.where(A==1,-sys.maxsize,A) 
    A = np.where(A==0,1,A) 
    return A