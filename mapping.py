from flask import Flask,  render_template
app = Flask(__name__) #Help out flask determine the root path

#@ signifies a decorator - way to wrap a function and and modify its behavior
@app.route('/')
@app.route('/<user>')
def index(user = None):
    return render_template("user.html", user=user)


if __name__ =="__main__":   #Quick check to run the app whenever this file is called directly
    app.run()     #Start with web server
