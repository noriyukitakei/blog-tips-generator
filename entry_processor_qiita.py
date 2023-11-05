import logging
import sys
import requests

# ログの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# StreamHandlerの設定
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.INFO)

# ハンドラをロガーに追加
logger.addHandler(handler)

def get_all_entries(url):
    all_articles = []
    page = 1
    per_page = 100

    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f'API request failed with status code: {response.status_code}')
        
        articles = response.json()
        if not articles:
            break
        
        for article in articles:
            # feedparserの形式に合わせた辞書を作成
            parsed_article = {
                'content': article['rendered_body'],
                'link': article['url']
            }
            all_articles.append(parsed_article)

        page += 1

    return all_articles

def get_system_role_for_extracting_image_url():
    return "Qiitaの場合は画像のリンクは、data-canonical-srcから取得して下さい。"
