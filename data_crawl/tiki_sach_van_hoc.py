from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import mlab
from models.book import Book
from no_accent_Vietnamese import convert

mlab.connect()

title = []
price_sale = []
image = []
linkBuy = []

for i in range(1,11):
    url = "https://tiki.vn/sach-van-hoc/c839?order=top_seller&src=mega-menu&page=" + str(i)

    html_content = urlopen(url).read().decode('utf-8')

    soup = BeautifulSoup(html_content, "html.parser")

    div_list = soup.find_all("div", "product-item")
    del div_list[3]

    for div in div_list:
        data_price = div['data-price']
        data_title = div['data-title']
        price_sale.append(data_price)
        title.append(data_title)
        a = div.a
        link = a['href']
        linkBuy.append(link)
        img = div.a.span.img
        image.append(img['src'])

for i in range(len(title)):
    new_book = Book(
        title = title[i],
        linkBuy = linkBuy[i],
        price_sale = price_sale[i],
        image = image[i],
        retailer = "Tiki",
        category = "Sách văn học",
        title_no_accent = convert(title[i])
        )
    new_book.save()
