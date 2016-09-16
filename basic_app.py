from flask import Flask, request, render_template

app = Flask(__name__) #Help out flask determine the root path


#@ signifies a decorator - way to wrap a function and and modify its behavior
@app.route('/') #root directory or home page
def index():
    return 'Method used: %s' % request.method

@app.route('/bacon', methods=['GET', 'POST']) #root directory or home page
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


if __name__ =="__main__":   #Quick check to run the app whenever this file is called directly
    app.run(debug=True)     #Start with web server
