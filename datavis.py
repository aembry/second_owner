import matplotlib
import matplotlib.pyplot as plt
import numpy


t = numpy.arange(0.0,2.0,0.01)
s = 1 + numpy.sin(2 * numpy.pi * t)

fig, ax = plt.subplots()
ax.plot(t,s)

ax.set(xlabel = 'time (s)', ylabel = 'voltage (mV',
        title = 'About as simple s it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()