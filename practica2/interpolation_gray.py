'''
Show all different interpolation methods for imshow
'''

import matplotlib.pyplot as plt
import numpy as np



np.random.seed(0)
grid = np.random.rand(4, 4)
print grid
plt.imshow(grid, interpolation='none', cmap='gray')
plt.show()
