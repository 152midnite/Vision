from glob import glob
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



def get_aswers(folder):
    files = glob(folder+'*.png')
    names = [file.split('/')[-1] for file in files]
    reg = '^[A-Z0-9]{7}'
    reg2 = '[A-Z0-9]{7}'
    plates = [re.search(reg,name)[0] for name in names if re.search(reg,name)]
    pictures = [file for file in files if re.search(reg2,file)]
    print(len(pictures),len(plates))
    all_files = glob(folder+'*')
    answers = []
    for plate in plates:
        for i,name in enumerate(all_files):
            if name.split('.')[1][-3:]== 'str':
                if re.search(plate,name):
                    y = 0
                    with open(name) as answer:
                        answer = answer.read().splitlines()[0]
                        answers.append((plate,answer))
    return answers

def write_answers(answers):
    with open('results','w') as results:
        for answer in answers:
            results.write(answer[0]+' '+answer[1]+'\n')

def fakenbullshet(name):
    with open(name,'r') as file:
        string = file.read()
    return string

def stripper(file_list):
    return [file.split('/')[-1] for file in file_list]

def get_files(folder,extension=''):
    return glob(folder+'*'+extension)

def draw_answer(file_label_pair,input_folder,output_folder,number,config_folder):
    text_file, img_name = file_label_pair
    img = Image.open(input_folder+img_name)
    text = fakenbullshet(config_folder+text_file)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Consolas-Bold.ttf',size=36)
    draw.text((0,36*number),text,(255,0,0),font=font)
    img.save(output_folder+img_name)



def get_unique(stripped_files):
    reg = '(.*)(\d)car'
    names_list = [re.findall(reg,name)[0][0] for name in stripped_files if re.findall(reg,name)]
    return sorted(set(names_list))

def izip_pngs(unique_names,file_names,extension):
    indx = 0
    stop = len(file_names)
    results = []
    for name in unique_names:
        length = len(name)
        while file_names[indx][:length]==name:
            length = len(name)
            indx+=1
            if indx >= stop:
                break
            if file_names[indx][-7:-4] == 'str':
                results.append((file_names[indx],name[:-1]+extension))
    return results

def draw_many(files_list,input_folder,output_folder):
    index = 0
    last_name = ''

    for file in files_list:

        if file[1] == last_name:
            index += 1
            print('names match')
        else:
            print('ARGH!')
            #print(file, ' ',last_name)
            index = 0

        if index > 0:
            draw_answer(file,output_folder,output_folder,index,input_folder)
        else:
            draw_answer(file,input_folder,output_folder,index,input_folder)

        last_name = file[1]



folder = './output_alpr/'

x = stripper(get_files(folder))
x.sort()
sorted_names = get_unique(x)



sets = izip_pngs(sorted_names,x,'.jpg')
draw_many(sets,'./original_images/','./output_drawing/')


