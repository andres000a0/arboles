def crearTabla(dataFrame, nombreTabla):
    archivoTabla = dataFrame.to_html()
    archivo = open(f"./tabla/{nombreTabla}.html", "w")  # dataFrame html vacio
    archivo.write(''' 
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Tabla</title>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;500;600&display=swap');
      /* Custom table styles */
      table {
        width: 100%;
        border-collapse: collapse;
        font-family: 'Poppins', sans-serif;
        font-size: 12px;
      }
  
      th, td {
        padding: 8px;
        border: 1px solid #ddd;
      }
  
      th {
        background-color: #f9f9f9;
        font-weight: bold;
      }
  
      tr:nth-child(even) {
        background-color: #f1f1f1;
      }
    </style>
        </head>
        <body>
    ''')
    archivo.write(archivoTabla)
    archivo.write('''
            </body>
            </html>
        ''')
    archivo.close()
