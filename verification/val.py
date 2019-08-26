from glob import glob
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

files = glob('./output_alpr/*.png')
names = [file.split('/')[-1] for file in files]
reg = '^[A-Z0-9]{7}'
reg2 = '[A-Z0-9]{7}'
plates = [re.search(reg,name)[0] for name in names if re.search(reg,name)]
pictures = [file for file in files if re.search(reg2,file)]
print(len(pictures),len(plates))
all_files = glob('./output_alpr/*')


answers = []

for plate in plates:
    for i,name in enumerate(all_files):
        if name.split('.')[1][-3:]== 'str':
            if re.search(plate,name):
                y = 0
                with open(name) as answer:
                    answer = answer.read().splitlines()[0]
                    answers.append((plate,answer))



with open('results','w') as results:
    for answer in answers:
        results.write(answer[0]+' '+answer[1]+'\n')

