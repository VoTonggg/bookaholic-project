from flask import *
from models.user import User
from models.book import Book
from no_accent_Vietnamese import convert
import mlab

app = Flask(__name__)
app.secret_key = "a super super secret key"
mlab.connect()

from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        sach_van_hoc = Book.objects(category = "Sách văn học")
        sach_kinh_te = Book.objects(category = "Sách kinh tế")
        manga_comics = Book.objects(category__icontains = "Truyện tranh, Manga")
        sach_tong_hop = Book.objects(category = "Sách kiến thức tổng hợp")
        sach_ngoai_ngu = Book.objects(category__icontains = "ngoại ngữ")
        session['sachvanhoc'] = len(sach_van_hoc)
        session['sachkinhte'] = len(sach_kinh_te)
        session['mangacomics'] = len(manga_comics)
        session['sachtonghop'] = len(sach_tong_hop)
        session['sachngoaingu'] = len(sach_ngoai_ngu)
        return render_template('index.html')
    else:
        form = request.form 
        title = form['title']
        title = convert(title)
        book_to_find = Book.objects(title_no_accent__icontains=title)
        return render_template("searchresult.html", book_to_find = book_to_find)

@app.route('/sign-up', methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        form = request.form 
        username = form['username']
        password = form['password']
        new_user = User(
            username = username,
            password = password
        )
        new_user.save()
        session['username'] = username
        return redirect(url_for("signin"))

@app.route('/sign-in', methods = ["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    else:
        form = request.form 
        username = form['username']
        password = form['password']
        # print(username)
        # print(password)
        user_to_find = User.objects(username = username, password = password)
        print(len(user_to_find))
        # print(user_to_find)
        if len(user_to_find) == 0:
            flash("You failed to log in !!! Please try again.")
            return redirect(url_for("signin"))
        else:
            session['loggedin'] = True
            session['username'] = username
            session['password'] = password
            return redirect(url_for("index"))

@app.route('/logout')
def logout():
    del session['loggedin']
    del session['username']
    del session['password']
    return redirect(url_for("index"))

@app.route('/book-category/<category>')
def bookcategory(category):
    if category == "Sách văn học":
        sach_van_hoc = Book.objects(category = "Sách văn học")
        session['current_category'] = "Sách văn học"
        return render_template("book_category.html", sach = sach_van_hoc)
    elif category == "Sách kinh tế":
        sach_kinh_te = Book.objects(category = "Sách kinh tế")
        session['current_category'] = "Sách kinh tế"
        return render_template("book_category.html", sach = sach_kinh_te)
    elif category == "Truyện tranh, Manga, Comic":
        manga_comics = Book.objects(category__icontains = "Truyện tranh, Manga")
        session['current_category'] = "Truyện tranh, Manga, Comic"
        return render_template("book_category.html", sach = manga_comics)
    elif category == "Sách tổng hợp": 
        sach_tong_hop = Book.objects(category = "Sách kiến thức tổng hợp")
        session['current_category'] = "Sách tổng hợp"
        return render_template("book_category.html", sach = sach_tong_hop)
    elif category == "Sách ngoại ngữ": 
        sach_ngoai_ngu = Book.objects(category__icontains = "ngoại ngữ")
        session['current_category'] = "Sách ngoại ngữ"
        return render_template("book_category.html", sach = sach_ngoai_ngu)

@app.route("/book-category")
def listbook():
    sach_van_hoc = Book.objects(category = "Sách văn học")
    session['current_category'] = "Sách văn học"
    return render_template("book_category.html", sach = sach_van_hoc)

# @app.route("/book-category/<category>/<int:page>")
# def listbook


if __name__ == '__main__':
  app.run(debug=True)
 