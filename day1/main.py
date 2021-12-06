import numpy
f = numpy.fromfile("input.txt", sep="\n")
f1 = f.copy()[1:]
f1 = numpy.append(f1, 0)
#part 1
print(len(list(filter(None, numpy.greater(f1, f)))))
f2 = f1.copy()[1:]
f2 = numpy.append(f2, 0)
pt = numpy.add(numpy.add(f1, f), f2)
pt2 = pt.copy()[1:]
pt2 = numpy.append(pt2, 0)
#part 2
print(len(list(filter(None, numpy.greater(pt2, pt)))))