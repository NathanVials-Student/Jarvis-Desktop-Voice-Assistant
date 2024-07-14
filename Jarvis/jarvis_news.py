#import dependencies
import feedparser

#import speak function
from jarvis_actions import speak


def read_headlines():
    #parse news feed
    news_feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml?edition=uk")
    entries = news_feed.entries

    #output top ten articles
    articles = []
    count = 0
    while count < 10:
        articles.append(entries[count])
        speak(articles[count].title)
        print(articles[count].title,":")
        print(articles[count].link)
        count += 1