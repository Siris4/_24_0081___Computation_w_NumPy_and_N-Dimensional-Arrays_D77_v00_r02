import numpy as np
import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a raccoon!
from PIL import Image  # for reading image files

# Create new ndarray from scratch
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

# Access the 3rd value in the 2nd row
print(array_2d[1,2])

# Access all the values in the first row
print(array_2d[0, :])
# array([1, 2, 3, 9])


