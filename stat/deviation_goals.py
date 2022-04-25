from scipy import stats
import numpy
import matplotlib.pyplot as plt
import math

goals = [8, 4, 8, 2, 4, 0, 2, 2, 5, 4, 4, 4, 8, 5, 6, 7, 2, 2, 4, 3, 5, 6, 4, 8, 7, 2, 7, 5]
a = numpy.array(goals)

print(numpy.median(a))  # 4.0
print(numpy.mean(a))  # 4.571428571428571
print(stats.mode(a))  # ModeResult(mode=array([4]), count=array([7]))

# range - размах (max-min)
print("размах: ", numpy.ptp(a))  # 8
print("min: ", numpy.nanmin(a))  # 0
print("max: ", numpy.nanmax(a))  # 8

# стандартное отклонение
print(numpy.std(a, ddof=1))  # 2.234884559593402
# какой процент наблюдений превосходит z-значение 4 (или вероятность такого значения): (4 - mean) / std
z = (4-numpy.mean(a))/numpy.std(a, ddof=1)
print(z)						# -0.2556859453772112
print(1 - stats.norm.cdf(z))  # 0.6009033257590559

x_sum = 0
for i in goals:
	x = (i - numpy.mean(a))**2
	x_sum = x_sum + x
print(x_sum)
dispersion = x_sum / len(goals)
sdeviation = math.sqrt(dispersion)
print("dispersion - ", dispersion, 'sdeviation - ', sdeviation)


plt.figure(1,figsize=(5,6))
plt.subplot(111)
plt.axis([0,2,-1,7])
plt.boxplot(a, showfliers=True)

plt.grid() # to draw horizontal grid lines
plt.show()
