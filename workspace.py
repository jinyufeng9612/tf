import numpy
data = numpy.random.rand(4,5)
print(data)
data = numpy.mat(data)
print(data)
data = data.A
print(data)