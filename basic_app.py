

# create a basic flask app that returns your name

from flask import Flask

# define the flask 

app = Flask(__name__)


# define a route
@app.route('/')
def home():
    return '<h2>My name is wanyetse charity </h2>'




































                                                                                                                                                                                                                                                                                                                                                                      