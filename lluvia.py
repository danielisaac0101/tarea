import xlrd # pip install xlrd
from Array import Array3D

def main():
    f=0
    g=0
   
    a3= Array3D(14,33,34)
    for anio in range(1985,2019,1):
        ruta='./precipitacion/'+str(anio)+ 'Precip.xls'
        #print(ruta)
        archivo= xlrd.open_workbook(filename=ruta)
        hoja= archivo.sheet_by_index(0)
        for r in range (1,33,1):
            for c in range (0,14,1):
                #print(hoja.cell_value(r,c), end='')
               # print(anio,r ,c)
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))
    a=int(input("anio(1985-2019):"))
    e=int(input("Estado(1-32):"))
    m=int(input("Mes(1-12): "))
    print(f"En el estado de", hoja.cell_value(e-34,0)+
          f" llovió un promedio de {a3.get_item(a-1985,e,m)} centimetros cubios en el mes de", hoja.cell_value(1,m-14)+
          f" del {a} ")
    print("____________________________________________________________")

# A partir del estado y mes, calcular el promedio de lluvias para ese estado, ese mes para todos los años. Desplegar el resultado en pantalla.

    for anio in range(1985,2019,1):
        f=(f+a3.get_item(anio-1985,e,m))
        g= f/34
    print(f"El promedio de las lluvias en el mes de", hoja.cell_value(1,m-14)+f"con un promdeio anual del: {g} ")
    print("____________________________________________________________")

#A partir del estado seleccionado, calcular el promedio de lluvias de todos los meses, en todos los años para ese estado.
    
    for anio in range(1985,2019,1):
        for r in range (1,13,1):
            f=(f+a3.get_item(anio-1985,e,m))
            g=(f/12)/34
    print("El promedio en el estado de",hoja.cell_value(e-34,0)+"en todos los meses de todos los años es de:",g)
    print("____________________________________________________________")
#Hacer el calculo de promedio total: Todos los estados, todos los meses para  todos los años.

    for anio in range(1985,2019,1):
        for r in range (1,13,1):
            for c in range (1,34,1):
                
                f=(f+a3.get_item(anio-1985,e,r))
                
                g= ((f/12)/34)/32
                
                
    print("El promedio total de todos los estados, todos los meses para todos los años es de:",g)
main()
