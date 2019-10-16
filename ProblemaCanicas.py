def suma(t1,t2):
    res_r=t1[0]+t2[0]
    res_i=t1[1]+t2[1]
    fin=(res_r,res_i)
    return fin

def multiplicacion(t1,t2):
    res_r=t1[0]*t2[0]+((t1[1]*t2[1])*-1)
    res_i=t1[0]*t2[1]+t1[1]*t2[0]
    fin=(res_r,res_i)
    return fin

def multi_mat_mat(mat1,mat2):
    mat_fin=[[(0,0)]*len(mat2[0]) for x in range(0,len(mat1))]
    aux=0
    if len(mat_fin)==1:
        aux=1
    for x in range(len(mat1)):
        for y in range(len(mat2[0])):
            for z in range(len(mat_fin)+aux):
                mat_fin[x][y]=suma(mat_fin[x][y],multiplicacion(mat1[x][z],mat2[z][y]))
    return mat_fin

def multi_vec_mat(vec,mat):
    mat_fin=[[0]*len(mat[0]) for i in range(0,len(vec))]
    for x in range(len(vec)):
        for y in range(len(mat[0])):
            for z in range(len(mat_fin)):
                mat_fin[x][y]+=vec[x][z]*mat[z][y]
    return mat_fin

def canicas_real(mat,vec,toques):
    fin=multi_vec_mat(mat,mat)
    toques-=1
    while True:
        if toques==0:
            break
        else:
            fin=multi_vec_mat(fin,mat)
            toques-=1
    return multi_vec_mat(fin,vec)

def canicas_imaginario(mat1,mat2,toques):
    fin=multi_mat_mat(mat1,mat1)
    toques-=1
    while True:
        if toques==0:
            break
        else:
            fin=multi_mat_mat(fin,mat1)
            toques-=1
    return multi_mat_mat(fin,mat2)


    
