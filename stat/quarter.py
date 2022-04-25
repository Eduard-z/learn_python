# box plot
import numpy
import matplotlib.pyplot as plt
import seaborn

data_to_plot = numpy.array([157,159,161,164,165,166,167,167,167,168,169,170,170,170,
                            171,171,172,172,172,172,173,173,175,175,177,178,178,179,185])

plt.figure(1,figsize=(5,6))
plt.subplot(111)
plt.axis([0,2,155,190])
plt.boxplot(data_to_plot, showfliers=True)

plt.grid() # to draw horizontal grid lines

# seaborn.boxplot(data_to_plot)
plt.show()


# Первый квартиль
print(numpy.quantile(data_to_plot, 0.25))
# Второй квартиль
print(numpy.quantile(data_to_plot, 0.50))
# Третий квартиль
print(numpy.quantile(data_to_plot, 0.75))
# Четвертый квартиль
print(numpy.quantile(data_to_plot, 1))
