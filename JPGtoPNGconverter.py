from PIL import Image
import os,sys
first = sys.argv[1]
last = sys.argv[2]
if os.path.isdir(last):
    print("This directory already exits")
else:
   os.mkdir(f'{last}')
obj = os.scandir(first)
for entry in obj:
    if entry.path.endswith('jpg'):
        filename = os.path.basename(entry)
        file, extension = os.path.splitext(filename)
        img = Image.open(entry.path)
        img.save(f'{last}/{file}.png',"png")
