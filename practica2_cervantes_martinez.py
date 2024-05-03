import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Leer el archivo y limpiar los datos
data = np.genfromtxt('airPollutants.csv', delimiter=',', skip_header=1, usecols=range(3, 14), missing_values='NA', filling_values=np.nan)
data_clean = data[~np.isnan(data).any(axis=1)].T

# Variables
column_names = ['O3', 'SO2', 'NO2', 'CO', 'PM10', 'PM2_5', 'TEMP', 'WS', 'WD', 'HR', 'PBAR']
contaminantes = ['O3', 'SO2', 'NO2', 'CO', 'PM10', 'PM2_5']
variables_atmosfericas = ['TEMP', 'WS', 'WD', 'HR', 'PBAR']

# Calcular estadísticas
mean_data = np.mean(data_clean, axis=1)
var_data = np.var(data_clean, axis=1)
cov_data = np.cov(data_clean, rowvar=False)

# Imprimir resultados
for i, name in enumerate(column_names):
    print(f"Media de {name}: {mean_data[i]}")
print('\n')
for i, name in enumerate(column_names):
    print(f"Varianza de {name}: {var_data[i]}")
print('\n')
for i, name1 in enumerate(column_names):
    for j, name2 in enumerate(column_names):
        print(f"Covarianza de {name1} y {name2}: {cov_data[i, j]}")

# Función para graficar dispersión con tendencia lineal
def scatter_with_trend(x, y, xlabel, ylabel):
    plt.scatter(x, y, label='Datos')
    slope, intercept, _, _, _ = linregress(x, y)
    plt.plot(x, slope * x + intercept, color='red', label='Tendencia')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Generar gráficas de dispersión
for contaminante in contaminantes:
    for variable in variables_atmosfericas:
        x = data_clean[column_names.index(variable)]
        y = data_clean[column_names.index(contaminante)]
        scatter_with_trend(x, y, variable, contaminante)

print("\n")
# Calcular y mostrar correlaciones
# Variables relevantes
variables_atmosfericas = ['TEMP', 'HR', 'PBAR']
contaminantes = ['O3', 'PM10']

# Calcular y mostrar correlaciones
for contaminante in contaminantes:
    for variable in variables_atmosfericas:
        correlation = np.corrcoef(data_clean[column_names.index(contaminante)], data_clean[column_names.index(variable)])[0, 1]
        print(f"Correlación entre {variable} y {contaminante}: {correlation}")

# Graficar diagramas de caja
plt.figure(figsize=(10, 6))
plt.boxplot([data_clean[column_names.index(variable)] for variable in ['PM2_5', 'TEMP', 'HR']], labels=['PM2.5', 'TEMP', 'HR'])
plt.title('Diagrama de Caja de PM2.5, TEMP y HR')
plt.xlabel('Variables')
plt.ylabel('Valores')
plt.grid(True)
plt.show()