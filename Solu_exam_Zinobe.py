# Solución Problemas Zinobe
# Librerías necesarias para los 4 problemas.
import sys
import numpy as np
from itertools import chain
import scipy.optimize as opt
from math import cos,sin, pi
# Esta función me convierte los elementos 0 en 1, y los elementos 1 en menos el máximo entero que puede tomar el sistema.
def convert_matriz(A):
    A = np.array(A, dtype=np.float)
    A = np.where(A==1,-sys.maxsize,A) 
    A = np.where(A==0,1,A) 
    return A
# Algoritmo de Kadane para arreglos en 2D.
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
# Función solucion para nuestro problema 1.
def maximo_rectangulo(M):
    try:
        if len(set(chain.from_iterable(M)))>2:
            return "La matriz posee números distintos de 1 y 0"
        elif set(chain.from_iterable(M)) == {1}:return (0,0,0,0)
        elif len(set(chain.from_iterable(M))) ==0 : 
            return "La matriz no posee elementos"
        len_col,len_row=len(M[0]),len(M)
        if len_col >= len_row:
            date = list(kadane(M,len_row, len_col))
            width = abs(date[1]-date[3])+1
            length= abs(date[2]-date[4])+1
            return date[2],date[1], width,length
        else:
            date = list(kadane(M,len_col, len_row))
            width = abs(date[1]-date[3])+1
            length = abs(date[2]-date[4])+1
            return date[2],date[1], width, length
    except ValueError:
        return "La matriz no cumple las condiciones"
# Función solucion para nuestro problema 2.
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
# Funciones elementales para mi problema 3:
# - La función element, me toma los elementos de la vecindad de mi celda.
# - La función neigh, me crea un conjunto con los indices de los elementos de la vecindad.
element = lambda M,row,col: [M[i][j] for i in range(row-1,row+2) for j in range(col-1,col+2)
                            if (0 <= i < len(M) and 0 <= j < len(M[0]))]
neigh   = lambda M,row,col: {(i,j) for i in range(row-1,row+2) for j in range(col-1,col+2)
                            if (0 <= i < len(M) and 0 <= j < len(M[0]))}
# Función solucion para nuestro problema 3.
def iterador_celdas_libres(M,row,col):
    try:
        if len(set(chain.from_iterable(M)))>2:
                return "La matriz posee números distintos de 1 y 0"
        elif len(set(chain.from_iterable(M))) ==0 : 
                return "La matriz no posee elementos"
        elif sum(element(M,row,col))!=0: return "No existe un camino"
        elif row>= len(M) or col >len(M[0]) or row<0 or col<0: return "Error en los indices"
        list_iter = []
        set_neigh = neigh(M,row,col)
        #calcular derecha 
        for i in range(col,-1,-1):
            for j in range(row,-1,-1):
                if sum(element(M,j,i)) ==0 and (j,i) in set_neigh:
                    list_iter.append((j,i))
                    set_neigh.update(neigh(M,j,i))
            for j in range(row+1,len(M)):
                if sum(element(M,j,i)) ==0 and (j,i) in set_neigh:
                    list_iter.append((j,i))
                    set_neigh.update(neigh(M,j,i))
        #claculo izq
        for i in range(col+1, len(M[0])):
            for j in range(row,-1,-1):
                if sum(element(M,j,i)) ==0 and (j,i) in set_neigh:
                    list_iter.append((j,i))
                    set_neigh.update(neigh(M,j,i))
        list_iter = iter(list_iter)
        return list_iter
    except ValueError:
        return "La matriz no cumple las condiciones"
    except TypeError:
         return "La matriz no cumple las condiciones"
# Solución problema plus.
def equation(variable):
    (N,t)= variable
    #constans
    mu, mass , gravity, acce = 0.2, 10, 10, 0.012
    w = mass*gravity
    #assignment
    F_r = N*mu
    w_x = w*sin(t) 
    w_y = w*cos(t)
    #Equation system
    system_q = [-F_r+w_x-mass*acce, N-w_y]
    return system_q
solution = opt.fsolve(equation, (0,2*pi) ) 
