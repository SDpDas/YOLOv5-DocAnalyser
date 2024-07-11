import os 
import random
import xml.etree.ElementTree as ET

xml_dir = 'C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\xml_files' #folder path to xml files (VOC format)
image_dir = "C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\Original" #folder path to all images

def get_image_path(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('path').text
    return filename

xml_files = [os.path.join(xml_dir, f) for f in os.listdir(xml_dir) if f.endswith('.xml')]
#get all XML files

image_paths = [os.path.join(xml_dir, get_image_path(xml_file)) for xml_file in xml_files]
#extracts image path from all the XML files

random.shuffle(image_paths) #shuffling dataset
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1
#splitting the dataset

num_image = len(image_paths)
train_split = int(num_image * train_ratio)
val_split = int(num_image * (train_ratio + val_ratio))
#gets split of no. of images in each folder type

train_paths = image_paths[:train_split]
val_paths = image_paths[train_split:val_split]
test_paths = image_paths[val_split:]
#gets indexes for all the image ranges

with open('C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\labels\\train.txt', 'w') as f:
    for path in train_paths:
        f.write(path + '\n')

with open('C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\labels\\val.txt', 'w') as f:
    for path in val_paths:
        f.write(path + '\n')

with open('C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\labels\\test.txt', 'w') as f:
    for path in test_paths:
        f.write(path + '\n')

#each function opens the file and writes the path according to their split