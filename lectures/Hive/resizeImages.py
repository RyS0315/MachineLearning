from PIL import Image
import os
import re
from glob import glob
import keras

minw = 10000000
minh = 10000000

path = "hive plots\\"
for filename in os.listdir(path):
  if filename.endswith('png'):
    im = Image.open(path + filename).convert('L')
    width, height = im.size
    # cw = round(width/2)
    # ch = round(height/2)
    # im = im.crop((cw-922, ch-754, cw+922, ch+754))
    
    if width < minw:
        minw = width
    if height < minh:
        minh = height
    print(width, height)
print(minw, minh)

for filename in os.listdir(path):
  if filename.endswith('png'):
    im = Image.open(path + filename).convert('L')
    width, height = im.size
    if height != minh:
        #resize according to height
        new_width = round(minh * width / height)
        im = im.resize((new_width, minh), resample = Image.ANTIALIAS)
        im = im.crop((round(width/2.0 - 780), 
                      round(height/2.0 - 650), 
                      round(width/2.0 + 780), 
                      round(height/2.0 + 650)))
        im.save("hive plots resized\\"+ filename[:-4] + "_g.png")

