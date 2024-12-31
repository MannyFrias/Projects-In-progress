from flask import Blueprint, render_template
from services.news_scraper import scrape_news

news_bp = Blueprint('news', __name__)

@news_bp.route('/news')
def news():
    articles = scrape_news()
    return render_template('home.html', articles=articles)