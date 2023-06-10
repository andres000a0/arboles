import pandas as pd
from helpers.tabla import crearTabla
from helpers.caucaciaBarras import graficaCaucacia


arboles = pd.read_csv('./Data/Siembras.csv')

filtro1 = arboles.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia"')
filtro2 = arboles.query('Arboles > 1 and Ciudad == "Caucasia"')
caucasia2 = arboles.query('Arboles > 1 and Hectareas > 1')
filtroRioArriba = arboles.query('Vereda == "Rio Arriba"')
filtroLaSalazar = arboles.query('Vereda == "La Salazar"')
Caramanta = arboles.query('Arboles > 100 and Ciudad == "Caramanta"')

#FILTRO 1--------------------------------
# crearTabla(filtro1,'SantaFeDeAntioquia')
# santaFe = arboles[(arboles['Arboles']> 1) & (arboles['Ciudad']=="Santa Fe de Antioquia")]
# graficaCaucacia(filtro1, 'Arboles', 'Hectareas', 'graficaSantafeDeAntioquia')
#FILTRO 2----------------------------------------------------------------
# caucasia = arboles[(arboles['Arboles']> 1) & (arboles['Ciudad']=="Caucasia")]
# crearTabla(caucasia,'Caucasia')
# crearTabla(filtro2,'Caucasia')
# graficaCaucacia(caucasia2, 'Arboles', 'Hectareas', 'graficaCaucasia')
# print(caucasia)
#FILTRO 3----------------------------------------------------------------
# crearTabla(filtroLaSalazar, 'La Salazar')
# crearTabla(filtroRioArriba, 'Rio Arriba')
#graficaCaucacia(filtroLaSalazar, 'Arboles', 'Hectareas', 'graficaLaSalazar')
# graficaCaucacia(filtroRioArriba, 'Arboles', 'Hectareas', 'graficaRioArriba')
#FILTRO 4----------------------------------------------------------------
# filtro = (arboles['Ciudad'] == 'Bello') & (arboles['Vereda'] == 'Quitasol')
# datos_quitasol = arboles[filtro]

# columnas_numericas = datos_quitasol.select_dtypes(include='number').columns
# estadisticas = datos_quitasol[columnas_numericas].describe()

# crearTabla(datos_quitasol, 'quitasol')
# graficaCaucacia(estadisticas, 'Arboles', 'Hectareas', 'graficaQuitasol')
# print(datos_quitasol)
#FILTRO 5--------------------------------------------------------
crearTabla(Caramanta, 'Caramanta')
graficaCaucacia(Caramanta, 'Arboles', 'Hectareas', 'graficaCaramanta')
print(Caramanta)






