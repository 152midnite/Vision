from glob import glob

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("/home/dante/work/db/verification/PJI5921_0car.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('Consolas-Bold.ttf',size=36)
draw.text((0, 0),"car",(255,255,255),font=font)
img.save('sample-out.jpg')

allImgFiles = glob('./output_alpr/*.png')
allFiles = glob('./output_alpr/*')
imgNames = [ImgFile.split('/')[-1] for ImgFile in allImgFiles]
justNames = [imgName.split('.')[0].split('/')[-1] for imgName in imgNames]

n = 5
print(justNames[0:n],'\n')
print(allFiles[0:n],'\n')
print(imgNames[0:n],'\n')
print(allImgFiles[0:n],'\n')
