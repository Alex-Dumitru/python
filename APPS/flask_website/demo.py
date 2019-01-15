from flask import Flask

app = Flask(__name__)      # instanciate the class that you imported
                           # the parameter will hold the name of the python script which is executed
'''
case 1: script executed directly    ->  __name__ = "__main__"
case 2: script is imported          ->  __name__ = "demo"
'''
@app.route('/')    #with this decorator we define the address pages of the website
def home():
    return "Home page goes here"     # content of the page is returned here

@app.route('/about/')
def about():
    return "Website content goes here (about)"

if __name__ == "__main__":
    app.run(debug=True)
