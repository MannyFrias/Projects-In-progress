import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    for item in soup.find_all('article'):
        title = item.find('h2').get_text() if item.find('h2') else 'No Title'
        link = item.find('a')['href'] if item.find('a') else 'No Link'
        summary = item.find('p').get_text() if item.find('p') else 'No Summary'
        
        articles.append({
            'title': title,
            'link': link,
            'summary': summary
        })

    return articles

def get_latest_news():
    news_sources = [
        'https://example-news-site.com',
        'https://another-news-site.com'
    ]
    
    all_articles = []
    for source in news_sources:
        all_articles.extend(scrape_news(source))
    
    return all_articles