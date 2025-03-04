#VISUALIZACION DE DATOS


"""MatPlotLib"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# crea un gráfico de líneas, años en el eje x, cantidades en el eje y
#primero definimos los valores que se grtaficaran en el eje X y Y
# luego definimos el color de la linea del grafico
#marker : indica que se usaran marcadores circulare para destacar los puntos de datos
# finalmente establecemos el estilo de linea
""" plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title(" Nominal GDP")
# añade una etiqueta al eje y
plt.ylabel("Billions of $")
# añade una etiqueta al eje y
plt.xlabel("Año Fiscal") """
#plt.show()

"""GRAFICO DE BARRAS"""
""" Es una buena eleccion cuando se desea mostrar como varia uan cierta cantidad a lo largo de un conjunto discreto de elementos
 """


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

num_oscars = [5, 11, 3, 8, 10]
# bar , primero definimos el rango de valores en el eje x , luego definimos los valores del eje X
""" plt.bar(range(len(movies)), num_oscars)
#titulo del grafico
plt.title("My Favorite Movies") 
#etiqueta del eje Y
plt.ylabel("# of Academy Awards")
#usado para personalizar las marcas en el eje X
#sirve para Cambia las posiciones y etiquetas de los valores en el eje X.
plt.xticks(range(len(movies)), movies) """
#plt.show()

"""HISTOGRAMA BUCKET"""

from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
#agrupar las notas en bucket por decil, pero pone 100 con los 90
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

""" plt.bar([x + 5 for x in histogram.keys()],histogram.values(),10 , edgecolor=(0,0,0))

plt.xticks([10 * i for i in
range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1Grades")
plt.show() """

"""OTRO EJEMPLO"""

mentions = [500, 505]

years = [2017, 2018]

""" plt.bar(years, mentions, 0.8)

plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")
#plt.ticklabel_format(useOffset=False)
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at the ‘Huge’ Increase!")
plt.show() """


"""GRAFICOS DE LINEAS"""


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
""" print(xs)

# Podemos hacer varias llamadas a plt.plot
# para mostrar varias series en el mismo gráfico
plt.plot(xs, variance, 'g-', label='variance') # línea continua
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # línea de puntos y guiones
plt.plot(xs, total_error, 'b:', label='total error') # línea de puntos
# Como asignamos etiquetas a cada serie,
# obtenemos una leyenda gratis (loc=9 significa "arriba centro")
plt.legend(loc=9)

plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()
 """ 

"""GRAFICOS DE DISPERSION"""

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i']


""" plt.scatter(friends,minutes)
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy=(friend_count, minute_count), xytext = (5,-5), textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show() """


test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren’t Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
#mejora la presicion de la variacion de los puntos
plt.axis("equal")
plt.show()



