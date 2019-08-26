from toxml import toxml, writexml, atoi, natural_keys
from glob import glob
import os
from PIL import Image
import numpy as np
import re
import sys

parentdir = os.path.dirname(os.path.realpath(__file__))+'/'
imagesdir = parentdir+sys.argv[1]
xmldir = parentdir+sys.argv[2]


coords = []
with open('./indianPlatesPoints.txt','r') as f:
    for line in f:
        coordsinstr = (line.strip('[ ] \n  ').split(','))
        coords.append([float(coord) for coord in coordsinstr])

fullpathfilelist = glob(imagesdir+'/*.bmp')
fullpathfilelist.sort(key=natural_keys)

filelist = [file.split('/')[-1] for file in fullpathfilelist]
filenames = [file.split('.')[0] for file in filelist]


for index, file in enumerate(fullpathfilelist):
    image = Image.open(file)
    shape = np.shape(image)
    imcoords = coords[index]
    xml = toxml(imcoords,file,shape)

    writexml(xml,filenames[index],xmldir)
    

