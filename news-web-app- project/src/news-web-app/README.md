# README.md

# News Web App

This project is a web application that parses the internet for news articles and displays them in small windows on the site. It includes user authentication features using Flask and SQL for database management.

## Features

- User registration and login
- Display of news articles in a user-friendly format
- Scraping of news articles from various sources

## Project Structure

```
news-web-app
├── src
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   └── register.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── main.js
│   ├── models
│   │   ├── user.py
│   │   └── article.py
│   ├── routes
│   │   ├── auth.py
│   │   └── news.py
│   ├── services
│   │   └── news_scraper.py
│   ├── database.py
│   └── app.py
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd news-web-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```
2. Open your web browser and go to `http://localhost:5000`.

## License

This project is licensed under the MIT License.