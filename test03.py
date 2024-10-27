import requests

# キーワード抽出APIのエンドポイントとAPIキー
KEYWORD_URL = "https://labs.goo.ne.jp/api/keyword"
ENTITY_URL = "https://labs.goo.ne.jp/api/entity"
API_KEY = "15add20bed94706f15292c3f2d3034c8217344db845b58eef05c9956826b0984"


def extract_keywords(title, body, max_num=5):
    """
    キーワード抽出を行い、キーワードの文字列リストを返す関数。
    """
    payload = {
        "app_id": API_KEY,
        "request_id": "test_keyword",
        "title": "旅行についての詳細情報 場所:"+title,
        "body": body,
        "max_num": max_num
    }

    try:
        response = requests.post(KEYWORD_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        # キーワードのキーを抽出
        return [list(keyword.keys())[0] for keyword in data.get('keywords', [])]
    except requests.exceptions.RequestException as e:
        print("キーワード抽出APIへのリクエストに失敗しました:", e)
        return []



def extract_entities(sentence, class_filter="PSN|LOC|DAT|TIM"):
    """
    固有表現抽出を行い、固有表現の文字列リストを返す関数。
    """
    payload = {
        "app_id": API_KEY,
        "request_id": "test_entity",
        "sentence": sentence,
        "class_filter": class_filter
    }

    try:
        response = requests.post(ENTITY_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return [entity[0] for entity in data.get('ne_list', [])]
    except requests.exceptions.RequestException as e:
        print("固有表現抽出APIへのリクエストに失敗しました:", e)
        return []


def translate_text(texts, target_language="EN"):
    # textsをリストとして受け取る
    api_key = "73d6082d-8d7c-01c8-d348-886cabc8db6f:fx"  # ここに取得したAPIキーを設定
    url = "https://api-free.deepl.com/v2/translate"
    translations = []  # 翻訳結果を格納するリスト

    for text in texts:
        params = {
            "auth_key": api_key,
            "text": text,
            "target_lang": target_language.upper()
        }
        response = requests.post(url, data=params)
        result = response.json()
        translations.append(result['translations'][0]['text'])  # 結果をリストに追加

    return translations



location = "旅行についての詳細情報"
prompt = "このコードはgooラボAPIを使って、テキストからキーワードを抽出します。沖縄"

keywords_result = extract_keywords(location, prompt)

entities_result = extract_entities(prompt)

result = [*keywords_result, *entities_result, location, prompt]

translated_texts = translate_text(result)
modified_prompt = ", ".join(translated_texts)
print(modified_prompt)
