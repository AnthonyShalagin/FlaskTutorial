from flask import Flask

app = Flask(__name__) #Help out flask determine the root path

@app.route('/') #root directory or home page
def index():
    return 'This is the homepage'

if __name__ =="__main__":   #Quick check to run the app whenever this file is called directly
    app.run(debug=True)     #Start with web server 
