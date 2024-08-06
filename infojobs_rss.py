import pandas as pd
import feedparser

rss_url = 'https://www.infojobs.net/trabajos.rss/kw_desarrollador/p_51/'

feed = feedparser.parse(rss_url)

print(feed)