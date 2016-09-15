from flask import Flask

app = Flask(__name__) #Help out flask determine the root path


#@ signifies a decorator - way to wrap a function and and modify its behavior
@app.route('/') #root directory or home page
def index():
    return 'This is the homepage'


@app.route('/tuna')
def tuna():
        return '<h2>SASHIMIIII</h2>'

@app.route('/profile/<username>') #brackets signify that a variable goes in between
def profile(username):
    return "Hey there %s" % username

@app.route('/post/<int:post_id>') #brackets signify that a variable goes in between
def show_post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

if __name__ =="__main__":   #Quick check to run the app whenever this file is called directly
    app.run(debug=True)     #Start with web server
