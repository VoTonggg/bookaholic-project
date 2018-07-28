from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import mlab
from models.book import Book
from no_accent_Vietnamese import convert


mlab.connect()

author = []
title = []
price_sale = []
image = []
linkBuy = []

for i in range(1,5):
    url = "https://tiki.vn/bestsellers/sach-thuong-thuc-doi-song/c862?p=" + str(i)

    html_content = urlopen(url).read().decode('utf-8')

    soup = BeautifulSoup(html_content, "html.parser")

    item_list = soup.find_all("div", "bestseller-cat-item")
    for item in item_list:
        data_brand = item['data-brand']
        data_price = item['data-price']
        data_title = item['data-title']
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
        category = "Sách kiến thức tổng hợp",
        title_no_accent = convert(title[i])
        )
    new_book.save()
