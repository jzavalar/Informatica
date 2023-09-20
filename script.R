# preparar los datos de manera local
if (file.exists('./Estudiantes.Rdata')) {
} else {  # cargar datos
  # cargar paquete rio
  library(rio)
  
  # datos en Internet
  url_data <- "https://github.com/hllinas/DatosPublicos/blob/main/Estudiantes.Rdata?raw=false"
  
  # copiar archivo de Internet al directorio local
  # nombres de los archivos
  archivo_rdata <- './Estudiantes.Rdata'
  archivo_csv <- './Estudiantes.csv'
  # copiar a Rdata
  convert(url_data,archivo_rdata)
  # copiar a csv
  convert(url_data,archivo_csv)
  
  # Renombrar el archivo
  # Checar si existe el archivo
  if(file.exists('./Estudiantes.csv')){
    file.copy('./Estudiantes.csv','./clipboard')
    #file.rename('./Estudiantes.csv','./clipboard')
  } else {
    print('Archivo no encontrado :')
  }
}
