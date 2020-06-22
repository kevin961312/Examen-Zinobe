from Solu_exam_Zinobe import maximo_cuadrado,maximo_rectangulo,iterador_celdas_libres
from random import randint
A= [[1,0,0,0],[1,0,0,0],[1,1,1,1],[1,1,1,1]]
B= [[1,0,0,0],[1,1,1,0],[1,1,1,1]]
C= [[1,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0]]
D= [[0,1],[1,0],[0,1]]
E= [[0,1,0,0,0,0,0,1,0,0],
     [1,0,0,0,0,1,0,0,0,0],
     [0,0,1,0,1,0,0,0,0,0],
     [1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,1,0,1,0,0,0],
     [0,0,1,0,0,0,0,0,1,0],
     [0,0,0,0,1,0,1,0,0,0]]
F= [[0,1,0,0,0,0,0,1,0,0],
     [1,0,0,0,0,1,0,0,0,0],
     [0,0,1,0,1,0,0,0,0,0],
     [1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,1,0,1,0,0,0],
     [0,0,1,0,0,0,0,0,1,0],
     [0,0,0,0,1,0,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]
     ]
G=[[0,0],[0,0],[1,1],[1,1]] 
H = [[1,0,0],[1,1,1]]
I = [[1,0,0],[1,0,1,0],[1,0,0],[1,1,1]]
J = [['a',1],[1,1]]
K = [[],[],[],[]]
list_pro = [A,B,C,D,F,E,G,H,I,J,K]
list_prov_MR = []
list_prov_MC = []
list_prov_iter = []
for i in list_pro:
    list_prov_MR.append(maximo_rectangulo(i))
for i in list_pro:
    list_prov_MC.append(maximo_cuadrado(i))

for i in list_pro:
    row = randint(0,len(i))
    col = randint(0,len(i[0]))
    try:
        if iterador_celdas_libres(i,int(row),int(col)).__class__.__name__ == 'list_iterator':
            list_prov_iter.append(next(iterador_celdas_libres(i,int(row),int(col))))
        else:
            list_prov_iter.append(iterador_celdas_libres(i,int(row),int(col)))
    except StopIteration:
        continue
import json
filename = 'data.json'
with open(filename, 'w') as f:
    json.dump(list_prov_MR, f)
    json.dump(list_prov_MC, f)
    json.dump(list_prov_iter, f)