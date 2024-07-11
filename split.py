import os
import shutil

base_dir = 'C:\\Users\\SAGAR DEEP\\Desktop\\Images_png'
image_dir = os.path.join(base_dir, 'images')
label_dir = os.path.join(base_dir, 'labels')
yolo_labels_dir = os.path.join(base_dir, 'yolo_labels')

os.makedirs(os.path.join(image_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(image_dir, 'val'), exist_ok=True)
os.makedirs(os.path.join(image_dir, 'test'), exist_ok=True)
os.makedirs(os.path.join(label_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(label_dir, 'val'), exist_ok=True)
os.makedirs(os.path.join(label_dir, 'test'), exist_ok=True)

def splittinger(file, split):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            image_path = line.strip()
            image_name = os.path.basename(image_path)
            label_name = os.path.splitext(image_name)[0] + '.txt'
        
            #copy and paste images into splitted training subfolders of image folder
            shutil.copy(image_path, os.path.join(image_dir, split, image_name))

            #copy labels from yolo_labels and split into training subfolder
            label_path = os.path.join(yolo_labels_dir, label_name)
            if os.path.exists(label_path):
                shutil.copy(label_path, os.path.join(label_dir, split, label_name))

splittinger(os.path.join(base_dir, 'train.txt'), 'train')
splittinger(os.path.join(base_dir, 'val.txt'), 'val')
splittinger(os.path.join(base_dir, 'test.txt'), 'test')

print("Data splitted succesfully. Check in Images_png folder of your desktop.")