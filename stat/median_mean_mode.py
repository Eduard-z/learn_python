from scipy import stats
import numpy
a = numpy.array([185,175,170,169,171,172,175,157,170,172,167,173,168,167,166,
                 167,169,172,177,178,165,161,179,159,164,178,172,170,173,171])

print(numpy.median(a))  # 170.5
print(numpy.mean(a))  # 170.4
print(stats.mode(a))  # ModeResult(mode=array([172]), count=array([4]))

# range - размах (max-min)
print("размах: ", numpy.ptp(a))  # 28
print("min: ", numpy.nanmin(a))  # 157
print("max: ", numpy.nanmax(a))  # 185

# стандартное отклонение
print(numpy.std(a, ddof=1))  # 6.0034472855472645
# какой процент наблюдений превосходит z-значение 175 (или вероятность такого значения): (175 - mean) / std = 0.77
print(1 - stats.norm.cdf(0.77))  # 0.22064994634264967

import statistics

a = [185,175,170,169,171,172,175,157,170,172,167,173,168,167,166,
     167,169,172,177,178,165,161,179,159,164,178,172,170,173,171]

print(statistics.mode(a))  # 172
# the following prints anticipate your comments, including possible ones, on the next steps
print(statistics.median(a))  # 170.5 - the next step
print(statistics.mean(a))  # 170.4 - the next step after the next one
# стандартное отклонение
print(statistics.stdev(a))  # 6.003447285547265
