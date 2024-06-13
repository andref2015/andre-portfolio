# news_digest.py
import os
import requests
import openai

def setup_api_keys():
    openai.api_key = os.environ['openai']
    news_api_key = os.environ['newsapi']
    return news_api_key

def get_news_headlines(news_api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}&sortBy=popularity&category=technology"

    result = requests.get(url)
    articles = result.json()["articles"]
    return articles[:3]  # Get the first three articles

def format_article_summary(articles):
    summaries = []
    sources = []

    for article in articles:
        title = article["title"][:80]  # Limit title to 80 characters
        source_name = article["source"]["name"]
        url = article["url"]
        summaries.append(f"{title}")
        sources.append(f"<a href = '{url}' target = '_blank'>{source_name}</a>")

    prompt = "Summarise these news articles in one VERY BRIEF paragraph (max 200 char), skip source names and separate each article summary with a period: "  + "; ".join(summaries)
    response = openai.chat.completions.create(model="gpt-4o", messages=[{"role": "user","content": prompt}])
    summary = response.choices[0].message.content
    
    hyperlinked_sources = "(Sources: " + ", ".join(sources) + ")"
    summary_with_sources = f"{summary} {hyperlinked_sources}"
    
    return summary_with_sources

def main():
    news_api_key = setup_api_keys()
    articles = get_news_headlines(news_api_key)
    summary_with_sources = format_article_summary(articles)
    return summary_with_sources
