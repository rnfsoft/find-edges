from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

filename = 'old.jpg'
im = Image.open(filename)
im_array = np.asarray(im)

def sqrt_diff(a,b):    
    return math.sqrt(sum((int(a[i])-int(b[i]))**2 for i in range(3))/3)

diff_threshold = 5
new_array = np.copy(im_array)
for row in range(im_array.shape[0]-1):
    for col in range(im_array.shape[1]-1):
        if ( sqrt_diff(im_array[row,col],im_array[row,col+1]) > diff_threshold
            or sqrt_diff(im_array[row,col],im_array[row+1,col]) > diff_threshold):
            new_array[row,col] = [0,0,0] # black
        else:
            new_array[row,col] = [255,255,255] # white
            
plt.imshow(new_array)
plt.savefig('new.jpg')