import requests

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

# 使用例
texts = ["沖縄行きました", "今日は良い天気です"]
translated_texts = translate_text(texts)
print(translated_texts)