from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
import sys
import mlab
from models.book import Book

# 0. Create connection
mlab.connect()

# 1. Download Webpage

#1.1 Create a connection

category = []
author = []
price_sale = []
title = []
linkBuy = []
image = []
for i in range(1,5):

    url = "https://tiki.vn/bestsellers-month/sach-truyen-tieng-viet/c316?p=" + str(i)
    #1.2
    html_content = urlopen(url).read().decode('utf-8')


    # 2. Extract ROI (region of interest)
    soup = BeautifulSoup(html_content, "html.parser")

    # extract Category
    item_list = soup.find_all("div", "bestseller-cat-item")
    for item in item_list:
        data_category = item['data-category']
        data_brand = item['data-brand']
        data_price = item['data-price']
        data_title = item['data-title']
        i = data_category[30:]
        for _ in range(len(i)):
            if i[_] == "/":
                i = i[:_]
                break
        category.append(i)
        author.append(data_brand)
        price_sale.append(data_price)
        title.append(data_title)

    link_list = soup.find_all("p", "image")
    for link in link_list:
        a = link.a
        img = link.a.img 
        linkBuy_each = a['href']
        linkBuy.append(linkBuy_each)
        image_each = img['src']
        image.append(image_each)

for i in range(len(title)):
    new_book = Book(
        title = title[i],
        linkBuy = linkBuy[i],
        price_sale = price_sale[i],
        image = image[i],
        author = author[i],
        retailer = "Tiki",
        category = category[i]
    )
    new_book.save()
