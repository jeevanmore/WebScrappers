from PIL import Image
import os


directory = input("Folder Path: ")
imagelist = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
         imlist = []
         imagelist.append(str(os.path.join(directory, filename)))
    
         continue
    else:
        continue

#print(imagelist)

imlist = []
im = ""

for image in imagelist:
    img = Image.open(image)
    im = img.convert('RGB')
    imlist.append(im)
       

#print(imlist)
img = imlist.pop(0)
img.save(r'C:\Users\jeevan\Desktop\WebScrappers\\myImages.pdf',save_all=True, append_images=imlist)
