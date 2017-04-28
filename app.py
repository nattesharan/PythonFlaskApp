from flask import Flask,redirect,url_for,request,render_template
app = Flask(__name__)
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
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))
@app.route('/result')
def result():
    a = {'phy':80, 'che':75, 'maths': 80, 'english': 78, 'Economics': 69, 'Biology': 84}
    return render_template('result.html', result = a)
if __name__ == '__main__':
   app.run(port=int("3000"),debug = True)