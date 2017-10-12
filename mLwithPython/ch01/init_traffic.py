import scipy as sp
import matplotlib.pyplot as plt
import init_error as er

data = sp.genfromtxt('web_traffic.tsv', delimiter='\t')
print(data)
x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
print(data.shape)

plt.scatter(x, y, s = 10)
plt.title("web traffic over last month")
plt.xlabel("Time")
plt.ylabel("Hits/hours")
plt.xticks([w * 7 * 24 for w in range(10)],
['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
#draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color='0.75')
plt.show()

# call er.error()

# Starting with a simple straight line
