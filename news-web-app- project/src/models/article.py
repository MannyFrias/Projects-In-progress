class Article:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __repr__(self):
        return f'<Article {self.title}>'

    def get_summary(self):
        return self.content[:100] + '...' if len(self.content) > 100 else self.content