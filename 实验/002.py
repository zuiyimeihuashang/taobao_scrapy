import numpy as np
n, k = map(int, input().split())
arr = np.fromstring(input(), dtype = np.uint32, sep=' ')
arr.sort()
print(arr[k])