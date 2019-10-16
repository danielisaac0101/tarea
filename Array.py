'''
ADT ABStract Dat Type
Basado en os tipos de datos basicos
Tienen un a estructura bien establecida
Tienen un numero de operaciones
'''
'''
ADT Arreglo
Un at que almacena valores del mismo tipo, pero diferenciazo por un indice
OPERACIONES:
Array(n)
legth() 
get_item(index,value)
'''

class Array:
    def __init__(self,n):
        self.__n=n
        self.__arreglo=[]
        for i in range(0,n,1):
            self.__arreglo.append(0)

    def length(self):
        return self.__n

    def get_item(self,index):
        return self.__arreglo[index]
    def set_item(self,index,value):
        self.__arreglo[index]=value
    def clearing(self,value):
        for i in range(0,self.__n,1):
            self.__arreglo[i] = value
    def to_string(self):
        print(f"Tamaño del arreglo ={self.__n}")
        print(self.__arreglo)
        
'''ADT areglo 2D
Es un ADTque almacena valores del mismo tipo agrupados en englones y columnas
similaraç a una tabla de excel

get_num_rows()
get_num_col()
clearing(value)
set_item(row,co,value)
get_item(row, co)
to_string()
'''
#Arreglo de dos dimensiones
class Array2D:
    def __init__(self,rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.__arreglo=[]
        for r in range(self.__rows):
            tmp=[]
            for c in range(self.__cols):
                tmp.append(0)
            self.__arreglo.append(tmp)
    def to_string(self):
        print(self.__arreglo)
    def get_num_rows(self):
        return self.__rows
    def get_num_cols(self):
        return self.__cols
    def set_item(self,rows,cols,value):
        self.__arreglo[rows][cols]=value
    def get_item(self,rows,cols,value):
        return self.__arreglo[rows][cols]
    def clearing(self,value):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__arreglo[i][j]=value

class Array3D:
    def __init__(self,depth,rows,cols):
        self.__depth=depth
        self.__rows=rows
        self.__cols=cols
        self.__arreglo=[[[0 for i in range(1,depth+1,1)] for i in range (1,rows+1,1)]for i in range(1,cols+1,1)]
        
    def get_num_cols(self):
        return self.__cols
    def get_num_rows(self):
        return self.__rows
    def get_num_depth(self):
        return self.__depth
    def set_item(self,depth,row,col,value):
        self.__arreglo[depth][row][col]=value
    def get_item(self,depth,row,col):
        return self.__arreglo[depth][row][col]
    def clearing(self,value):
        for i in range(self.__depth):
            for a in range(self.__rows):
                for c in range(self.__cols):
                    self.__arreglo[i][a][c]
    def to_string(self):
        capa=0
        for layer in self.__arreglo:
            print(f"---capa---{capa}")
            for ren in layer:
                print(ren)
            capa+=1

                    
        
    
    
    






