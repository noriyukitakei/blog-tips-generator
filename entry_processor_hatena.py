import logging
import sys
import feedparser
import requests
from requests.auth import HTTPBasicAuth
import os

# ログの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# StreamHandlerの設定
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# ハンドラをロガーに追加
logger.addHandler(handler)

def get_all_entries(url):
    logger.info(f"Fetching all entries from: {url}")
    
    username = os.environ.get("HATENA_ID")
    password = os.environ.get("HATENA_API_KEY")

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # responseを文字列として格納
    response_text = response.text
    all_entries = []
    feed = feedparser.parse(response_text)
    entries = feed.entries
    for entry in entries:
        link = [link.href for link in entry.links if link.rel == 'alternate']
        content = [content.value for content in entry.content if content.type == 'text/html']
        if not link or not content:
            continue
        all_entries.append({'content': content[0], 'link': link[0]})

    next_link = [link.href for link in feed.feed.links if link.rel == 'next']
    if next_link:
        all_entries.extend(get_all_entries(next_link[0]))

    return all_entries

def get_system_role_for_extracting_image_url():
    return ""