from flask import Blueprint, render_template, request, redirect, url_for
from models.articles import Article

def articles_blueprint(mongo):
    articles = Blueprint('articles', __name__, template_folder='templates')

    @articles.route('/')
    def index():
        articles = mongo.db.articles.find()
        return render_template('views/articles/index.html', articles=articles)

    @articles.route('/new', methods=['GET', 'POST'])
    def new():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            article = Article(title, content)
            mongo.db.articles.insert_one(article.__dict__)
            return redirect(url_for('articles.index'))
        return render_template('views/articles/new.html')

    return articles
