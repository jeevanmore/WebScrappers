from bs4 import BeautifulSoup
import requests
import os


url = input("Enter URL: ")

mkfolder = input("Create Folder: ")

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

links = []

img_tags = soup.select('img[src]')

for img in img_tags:
    links.append(img['src'])

#for l in links:
#    print(l)
   
os.mkdir(mkfolder)
for index, img_link in enumerate(links):
    img_data = requests.get(img_link).content
    with open(mkfolder+'/'+str(index)+'.jpg', 'wb+') as f:
        f.write(img_data)

