import os 
import glob
#Handles file paths and file searching 
import xml.etree.ElementTree as ET #Only to parse XML files

def convert_voc_to_yolo(xml_path, yolo_path, classes):
    tree = ET.parse(xml_path) #Parses the XML file
    root = tree.getroot()   #Gets root element of XML file
    image_id = os.path.basename(xml_path).split('.')[0] #Extracts basename of XML file to use as image ID
    yolo_txt_path = os.path.join(yolo_path, image_id + '.txt') #Adds the image to yolo path in YOLO format

    with open(yolo_txt_path, 'w') as f: 
        for obj in root.findall('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            #above snippet finds and checks for classes in each image

            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            #Extracts bounding box co-ordinates

            dw = 1.0 / float(root.find('size').find('width').text) #calculates width scaling factor
            dh = 1.0 / float(root.find('size').find('height').text) #calculates height scaling factor

            x = (b[0] + b[1]) / 2.0 - 1 #X coordinate of the bounding box
            y = (b[2] + b[3]) / 2.0 - 1 #Y coordinate of the bounding box

            w = b[1] - b[0] #width of the bounding box
            h = b[3] - b[2] #height of the boudning box

            x = x * dw
            w = w * dw
            y = y * dh  
            h = h * dh
            #Normalizes the co-ordinates
    
            f.write(f"{cls_id} {x} {y} {w} {h} \n")
            #writes class ID and normalized co-ordinates of YOLO file

def convert_annotations(xml_path, yolo_path, classes):
    if not os.path.exists(yolo_path):
        os.makedirs(yolo_path)
    xml_files = glob.glob(os.path.join(xml_path, '*.xml')) #Gets all XML files from its directory
    for xml_file in xml_files:
        convert_voc_to_yolo(xml_file, yolo_path, classes)

xml_path = 'C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\xml_files'
yolo_path = 'C:\\Users\\SAGAR DEEP\\Desktop\\Images_png\\yolo_labels'
classes = ['Title', 'Subtitle', 'Author', 'Sources', 'Text', 'Figure', 'Caption', 'Table', 'Page Number', 'References']

convert_annotations(xml_path, yolo_path, classes)