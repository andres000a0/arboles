import matplotlib.pyplot as plt

def graficaCaucacia(dataframe, campoY, campoX, nombreGrafica):
    plt.figure(figsize=(10, 6))
    colores = ['orange', 'green', 'purple']
    caucaciaPromedio = dataframe.groupby(campoX)[campoY].mean()
    plt.bar(caucaciaPromedio.index, caucaciaPromedio, color=colores)
    plt.title('Caucacia')
    plt.xlabel('Arboles')
    plt.ylabel('Hectareas')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'./assets/img/{nombreGrafica}.png')


