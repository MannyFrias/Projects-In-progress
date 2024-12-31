import requests
from bs4 import BeautifulSoup

def scrape_news():
    articles = []
    # Example sources - you can add more
    sources = [
        'https://news.google.com/rss',
        'https://feeds.bbci.co.uk/news/rss.xml'
    ]
    
    for source in sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        for item in items[:5]:  # Get first 5 articles from each source
            article = {
                'title': item.title.text,
                'link': item.link.text,
                'description': item.description.text if item.description else '',
                'date': item.pubDate.text if item.pubDate else ''
            }
            articles.append(article)
            
    return articles