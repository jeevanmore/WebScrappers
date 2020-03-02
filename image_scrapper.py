from bs4 import BeautifulSoup as bs
import requests
import os

url = input("Enter url: ")

mkfolder = input("Create Folder: ")

page = requests.get(url)

soup = bs(page.content, 'html.parser')

links = []

img_list = soup.select('img[src]')

for img in img_list:
    links.append(img['src'])

os.mkdir(mkfolder)

for index, img_link in enumerate(links):
    image_data = requests.get(img_link).content
    with open(mkfolder+'/'+str(index)+'.jpg', 'wb+') as f:
        f.write('img_data')

