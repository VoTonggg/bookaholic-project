from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
import sys
from flask import *
import mlab
from models.book import Book

# 0. Create connection
mlab.connect()

# 1. Download Webpage

#1.1 Create a connection

a_list_of_dict = []
for i in range(2,4):

    url = "https://tiki.vn/bestsellers/sach-truyen-tieng-viet/c316?p=" + str(i)
    #1.2
    html_content = urlopen(url).read().decode('utf-8')


    # 2. Extract ROI (region of interest)
    soup = BeautifulSoup(html_content, "html.parser")

    item_list = soup.find_all("p", "title")
    title = []
    link = []
    for p in item_list:
        title.append(p.a.contents[0].strip())
        link.append(p.a['href'])
    # print(link)

    item_list = soup.find_all("p", "price-sale")
    price = []
    for p in item_list:
        price.append(p.contents[0].strip())
    # print(price)

    item_list = soup.find_all("img", "img-responsive")
    print(item_list)
    image = []
    for img in item_list:
        image.append(img["src"])
    print(image)

    for i in range(len(title)):
        dic = {}
        dic['title'] = title[i]
        dic['link'] = link[i]
        dic['price'] = price[i]
        dic['image'] = image[i]
        a_list_of_dict.append(dic)


        new_book = Book(
        name = dic['title'],
        img = dic['image'],
        link = dic['link'],
        price = dic['price']
        )

        new_book.save()

# pyexcel.save_as(records = a_list_of_dict, dest_file_name="tiki.xlsx")