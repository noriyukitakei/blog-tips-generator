import logging
import sys
import feedparser

# ログの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# StreamHandlerの設定
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# ハンドラをロガーに追加
logger.addHandler(handler)

def get_all_entries(url):
    all_entries = []
    logger.info(f"Fetching all entries from feed: {url}")
    url = f"{url}?all=1"
    feed = feedparser.parse(url)
    entries = feed.entries
    if not entries:
        logger.info(f"No more entries found. Exiting.")
    else:
        for entry in entries:
            # 各エントリからcontentとlinkを抽出し、辞書に格納
            all_entries.append({'content': entry.summary, 'link': entry.link})

    return all_entries

def get_system_role_for_extracting_image_url():
    return ""