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
    current_page = 1
    max_iterations = 500 # 最大ループ回数を設定しておく

    logger.info(f"Fetching all entries from feed: {url}")
    while True:
        feed_url = f"{url}?paged={current_page}"
        feed = feedparser.parse(feed_url)
        entries = feed.entries
        if not entries:
            logger.info(f"No more entries found at page {current_page}. Exiting.")
            break
        for entry in entries:
            # 各エントリからcontentとlinkを抽出し、辞書に格納
            all_entries.append({'content': entry.content[0].value, 'link': entry.link})
        logger.info(f"Fetched {len(entries)} entries from page {current_page}.")
        current_page += 1
        if current_page > max_iterations:
            logger.info("Reached maximum number of iterations")
            break  # 最大ループ回数に達したらループを終了

    return all_entries

def get_system_role_for_extracting_image_url():
    return ""