from flask import Flask,redirect,url_for,request,render_template,make_response,abort,flash
from werkzeug import secure_filename
import random
from flask_mail import Mail,Message
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'abcd@gmail.com'
app.config['MAIL_PASSWORD'] = '**************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
secret = ''
for i in range(0,10):
    secret += str(random.randint(0,9))
app.secret_key = secret
@app.route('/hello/<name>')
def index(name):
    # a = "Hello "+ name
    # return a
    return render_template('dynamic.html',name = name) #send the name value to the html file
@app.route('/')
def home():
    return '<html><body><h1><strong><i>Hello, this is home</i></strong></h1></body></html>'
@app.route('/temp')
def temp():
    return render_template('simple.html')
@app.route('/hello/<int:no>')
def display(no):
    # return "Number is %d" % no
    return render_template('conditionals.html', no = no)
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest
@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))
@app.route('/success/<name>')
def success(name):
    return 'Hello %s welcome !!' % name
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        if user == 'admin':
            return redirect(url_for('success', name = user))
        else:
            abort(401)
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))
@app.route('/result')
def result():
    a = {'phy':80, 'che':75, 'maths': 80, 'english': 78, 'Economics': 69, 'Biology': 84}
    return render_template('result.html', result = a)
@app.route('/event')
def event():
    return render_template('alert.html')
@app.route('/student')
def student():
    return render_template('student.html')
@app.route('/studentresult', methods = ['POST', 'GET'])
def studResult():
    if request.method == 'POST':
        result = request.form
        # print(result)
        return render_template('studresult.html', result = result)
@app.route('/cookie')
def cookie():
    return render_template('addcookie.html')
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        name = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('Name',name)
        return resp
@app.route('/showcookie')
def showcookie():
    name = request.cookies.get('Name')
    return '<h1>Welcome ' + name + '!</h1>'
@app.route('/session')
def initial():
    if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/signout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/signin'></b>" + \
      "click here to log in</b></a>"
@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('initial'))
    return '''<form action = "" method = "post">
      <p><input type ="text" name = "username"/></p>
      <p><input type = 'submit' value = "Login"/></p>
      </form>'''
@app.route('/signout')
def logout():
    session.pop('username', None)
    return redirect(url_for('initial'))
@app.route('/flash')
def flash():
    return render_template('index.html')
@app.route('/signinn', methods = ['GET', 'POST'])
def signinn():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('flash'))
    return render_template('login.html', error = error)
@app.route('/upload')
def upload():
    return render_template('upload.html')
@app.route('/uploader',methods = ['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "<h1>File uploaded successfully</h1>"
@app.route('/email')
def sendemail():
    msg = Message('HELLO ! Sent from python Flask App', sender = 'abcd@gmail.com', recipients = ['egghhg@gmail.com'])
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return '<h1><i>Mail Sent</i></h1>'
if __name__ == '__main__':
   app.run(port=int("3000"),debug = True)