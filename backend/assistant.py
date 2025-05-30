import wikipedia
import datetime
import pyjokes
from newsapi import NewsApiClient

# Replace this with your actual API key from newsapi.org
newsapi = NewsApiClient(api_key='edde130a23814429b001603ac379d47a')

def speak(text):
    print("Assistant says:", text)  # For Flask server use, not voice

def get_news():
    try:
        top_headlines = newsapi.get_top_headlines(country='in', language='en', page_size=5)
        news_list = []
        for article in top_headlines['articles']:
            news_list.append(article['title'])
        return news_list
    except Exception as e:
        return ["Sorry Papa Jii, news fetch karne me dikkat aa rahi hai."]

def process_query(query):
    query = query.lower()

    if "time" in query:
        return datetime.datetime.now().strftime("The time is %H:%M:%S")

    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except Exception:
            return "Sorry Papa Jii, I couldn't find that."

    elif "joke" in query:
        return pyjokes.get_joke()

    elif "news" in query or "latest news" in query:
        news_items = get_news()
        return "\n".join(news_items)

    elif "play" in query:
        song = query.replace("play", "").strip()
        return f"Playing {song} on YouTube..."

    else:
        return "Sorry Papa Jii, I didn't get that."
