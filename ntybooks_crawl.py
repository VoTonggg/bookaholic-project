from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
import sys

# 1. Download Webpage

#1.1 Create a connection

a_list_of_dict = []
for i in range(1,2):

    url = "http://www.ntybooks.com/z/nty/top/" + str(i)
    #1.2
    html_content = urlopen(url).read().decode('utf-8')


    # 2. Extract ROI (region of interest)
    soup = BeautifulSoup(html_content, "html.parser")

    item_list = soup.find_all("div","product-meta")
    # print(item_list)
    title = []
    link = []
    for div in item_list:
        title.append(div.h3.a.string.strip())
        link.append(div.h3.a['href'])
    print(link)
    print(title)

    item_list = soup.find_all("span", "amount")
    price = []
    for span in item_list:
        price.append(span.string.strip())
    # print(price)

    item_list = soup.find_all("a", "thumb")
    image = []
    for a in item_list:
        image.append(a.img["src"])
    # print(image)

    # a_list_of_dict = []
    for i in range(len(title)):
        dic = {}
        dic['title'] = title[i]
        dic['link'] = link[i]
        dic['image'] = image[i]
        dic['price'] = price[i]
        a_list_of_dict.append(dic)

pyexcel.save_as(records = a_list_of_dict, dest_file_name="ntybooks.xlsx")