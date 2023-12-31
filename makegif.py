
"""
Created on Sun Dec  4 17:25:16 2022

@author: X415EP
"""

import imageio
images = []
filenames = []

for hr in range(3,17):
    for min in range(0,60,10):
        name = "radar"+"{:0>2d}".format(hr)+"{:0>2d}".format(min)+".jpg"
        filenames.append(name)

print(filenames)
       

with imageio.get_writer('1202.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

print("successful")
