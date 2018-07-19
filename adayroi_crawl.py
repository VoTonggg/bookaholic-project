from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
import sys

# 1. Download Webpage

#1.1 Create a connection

a_list_of_dict = []
for i in range(3):

    url = "https://www.adayroi.com/sach-c1384?q=%3Arelevance&page=" + str(i)
    #1.2
    html_content = urlopen(url).read().decode('utf-8')


    # 2. Extract ROI (region of interest)
    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup.prettify())
    # urlretrieve(url,"adayroi.html")

    item_list = soup.find_all("a","product-item__info-title")
    # print(item_list)
    title = []
    link = []
    for a in item_list:
        title.append(a.string.strip())
        link.append('https://www.adayroi.com' + a['href'])
    print(link)
    print(title)

    item_list = soup.find_all("span", "product-item__info-price-sale")
    price = []
    for span in item_list:
        price.append(span.string.strip())
    # print(price)
    # class="default lazy swiper-lazy "
    item_list = soup.find_all("img", "default lazy swiper-lazy ")
    print(item_list)
    image = []
    for img in item_list:
        image.append(img["data-src"])
    print(image)

    for i in range(len(title)):
        dic = {}
        dic['title'] = title[i]
        dic['link'] = link[i]
        dic['price'] = price[i]
        dic['image'] = image[i]
        a_list_of_dict.append(dic)

pyexcel.save_as(records = a_list_of_dict, dest_file_name="adayroi.xlsx")