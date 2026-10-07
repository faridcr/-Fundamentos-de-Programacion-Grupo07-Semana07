#Enunciado7 –PARSEAR DATOS CSV MANUALMENTE

lineas = [ "Kevin,18,Lima", "Maria,16,Cusco", "Carlos,20,Arequipa" ]
for linea in lineas:
    datos = linea.split(",")
    print(f"Nombre: {datos[0]}, Nota: {datos[1]}, Ciudad: {datos[2]}")



    