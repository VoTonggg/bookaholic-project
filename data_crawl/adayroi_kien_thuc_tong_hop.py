from urllib.request import urlopen, urlretrieve, Request
from bs4 import BeautifulSoup
from models.book import Book
from no_accent_Vietnamese import convert
import mlab

mlab.connect()

title = []
price_sale = []
image = []
linkBuy = []

for i in range(10):

    url = "https://www.adayroi.com/sach-ky-nang-song-kien-thuc-c1386?q=%3Abestselling-desc&page=" + str(i)
    #1.2
    rep = Request(url, data=None, headers= {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })



    html_content = urlopen(rep).read().decode("utf-8")


    # 2. Extract ROI (region of interest)
    soup = BeautifulSoup(html_content, "html.parser")

    a_list = soup.find_all('a', "product-item__thumbnail")

    for a in a_list:
        linkBuy_each = "https://www.adayroi.com" + a['href']
        linkBuy.append(linkBuy_each)
        img = a.img
        title.append(img['title']) 
        image.append(img['data-src'])

    price_list = soup.find_all("span", "product-item__info-price-sale")
    for p in price_list:
        price = p.string
        price = price[0:len(price)-1]
        price = price.replace(".","")
        price_sale.append(price)

for i in range(len(title)):
    new_book = Book(
        title = title[i],
        linkBuy = linkBuy[i],
        price_sale = price_sale[i],
        image = image[i],
        retailer = "Adayroi",
        category = "Sách kiến thức tổng hợp",
        title_no_accent = convert(title[i])
        )
    new_book.save()