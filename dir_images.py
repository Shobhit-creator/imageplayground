from PIL import Image, ImageFilter
import os

##for every item in X folder that ends in X, apply a basic blur to the image##

for entry in os.scandir('./Pokedex'):
    if entry.path.endswith('.jpg'):
        img = Image.open(entry.path)
        img = img.filter(ImageFilter.BoxBlur(2))

        img.show()

        ##and then re-save each of those new images under a new filename##

        # Split our original filename into name and extension
        (name, extension) = os.path.splitext(entry.path)

        # Save with "_blur" added to the filename
        img.save(name + '_blur' + extension)
        print(name)
        #img.save("./"+'_blur.jpg')
        # Save the image as a BMP
        img.save(name + '.bmp')