# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:27:38 2017

@author: w1406
"""
from PIL import Image
import glob, os
#os.chdir()
for file in glob.glob("*[cropped].tif"):
    os.remove(str(file))

for file in glob.glob("*.tif"):
    if '[cropped]' in file:
        continue
    im = Image.open(file)
    half_the_width=im.size[0]/2
    half_the_height=im.size[1]/2
    
    newimage=im.crop((0,0,645,484))
    newfile=file[:-4]+"[cropped]"+".tif"
    newimage.save(newfile) 
    

#    source="./"+name
#    destination="./vac"+str(i+1)+"/vasp.in"
#    os.rename(source, destination)