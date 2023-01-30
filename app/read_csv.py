import csv
#Lectura de un archivo CSV que contiene datos de poblacion de todos los paises del mundo

def read_csv(path): #funcion para leer el archivo csv
  with open(path,'r') as csvfile: #'r' indica que solo se permite leer
    reader = csv.reader(csvfile,delimiter = ',') 
    header = next(reader) #Se guarda en header el encabezado que contiene los nombres de las columnas del csv file
                            
    data=[]  
    for row in reader:
      iterable = zip(header,row) #La funcion zip agrupa iteradores en un objeto zip que contiene tuplas, agrupa los iteradores que estan en la misma posicion
      country_dict = {key:value for key,value in iterable}
      data.append(country_dict)
    return data
      
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)

 