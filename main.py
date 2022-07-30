import numpy as np
import pandas as pd
import csv


firstarr = np.arange(1, 1000, 3)


newdf = pd.DataFrame(firstarr)
print(newdf)
newdf.to_csv('source.csv', sep=',')

A = list()

A.append([234, 34, 54, 13, 95])

A.insert(2, 54)
print(A)
A.insert(0, 1000)
print(A)
A.reverse()
print(A)
d = A.count(1000)
print(d)
d = A.index(1000)
print(d)
origlist = [213, 12, 15, 259]
origlist.sort()
print(origlist)
origlist = origlist + ['cat', 'muse', 'hugo']
print(origlist)


def getArray(array1, array2):
    endarray = array1 + array2
    endarray.append("Has finished")
    return endarray


B = [34, 'dfgdfg', 'dfgf', 229]

func = getArray(A, B)
print(func)
