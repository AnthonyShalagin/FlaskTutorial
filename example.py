from flask import Flask,  render_template
app = Flask(__name__) #Help out flask determine the root path

#@ signifies a decorator - way to wrap a function and and modify its behavior
@app.route('/profile/<name>') #root directory or home page
def profile(name):
    return render_template("profile.html", name = name)


if __name__ =="__main__":   #Quick check to run the app whenever this file is called directly
    app.run()     #Start with web server
