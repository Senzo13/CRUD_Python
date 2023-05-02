from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from models.articles import Article
from controllers.articles_controller import articles_blueprint
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pycrud"
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello, World!'

app.register_blueprint(articles_blueprint(mongo), url_prefix='/articles')

if __name__ == '__main__':
    app.run(debug=True)
