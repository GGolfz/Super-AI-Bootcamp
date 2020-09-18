import numpy as np
a = [5,7,2,3,4,2,2,4,4,6,8,9,3,2,4,6,8,9,0,12,4,5,2,3,21,23,57,23,99]
# User Library
print(max(a))
# Linear Search
m = -99999
for i in a:
    if i > m:
        m = i
print(m)
# numpy max
print(np.max(a))