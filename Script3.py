import matplotlib.pyplot as plt

def funcion_cuadratica(x):
    return x**2

x_valores = range(-10, 11)
y_valores = [funcion_cuadratica(x) for x in x_valores]

# Crear la gráfica
plt.plot(x_valores, y_valores, label="Función Cuadrática")

# Configurar etiquetas y título
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfica de una Función Cuadrática")

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
