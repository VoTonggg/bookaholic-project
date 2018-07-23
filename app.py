from flask import *
from models.user import User
import mlab

app = Flask(__name__)
app.secret_key = "a super super secret key"
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
  app.run(debug=True)
 