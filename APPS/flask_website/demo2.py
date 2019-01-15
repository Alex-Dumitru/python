from flask import Flask, render_template

#render_template accesses an html file, stored somewhere in the directory files, and then displays that file on the requested URL
#actually all the html templates need to be present in the 'templates' folder in your projects directory
app = Flask(__name__)      # instanciate the class that you imported
                           # the parameter will hold the name of the python script which is executed
'''
case 1: script executed directly    ->  __name__ = "__main__"
case 2: script is imported          ->  __name__ = "demo"
'''
@app.route('/')    #with this decorator we define the address pages of the website
def home():
    return render_template("home2.html")

@app.route('/about/')
def about():
    return render_template("about2.html")

if __name__ == "__main__":
    app.run(debug=True)
