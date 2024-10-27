import requests
import time

def generate_image(prompt, token, output_path="output_image.jpeg", retries=5, wait_time=120):
    """
    Stability AI APIを使用してプロンプトから画像を生成します。

    Args:
        prompt (str): 画像生成に使用するプロンプト。
        token (str): Stability AI APIトークン。
        output_path (str): 生成した画像を保存するパス。
        retries (int): モデルが読み込み中の場合の再試行回数。
        wait_time (int): 再試行の間隔（秒）。
    Returns:
        None
    """
    api_url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "authorization": f"Bearer {token}",  # 認証に使用するAPIトークン
        "accept": "image/*"  # 画像フォーマットを指定
    }
    data = {
        "model_id": "sd3.5-large-turbo",
        "prompt": prompt,  # 生成プロンプト
        "output_format": "jpeg",  # 画像の出力フォーマット
        "height": 720,
        "width": 720,
        "samples": 1,
        "steps": 40,
        "aspect_ratio": "16:9"
    }

    # モデル読み込み中のステータスに対する再試行のためのループ
    for attempt in range(1, retries + 1):
        print(f"APIリクエストを送信中... (試行 {attempt}/{retries})")
        response = requests.post(api_url, headers=headers, files={"none": ''}, data=data)
        
        if response.status_code == 200:
            # リクエストが成功した場合、画像を保存して終了
            with open(output_path, 'wb') as file:
                file.write(response.content)
            print(f"画像が {output_path} に保存されました。")
            return
        elif response.status_code == 503:
            # モデルがロード中の場合の処理
            print(f"モデルがロード中です。{wait_time}秒後に再試行します...")
            time.sleep(wait_time)
        else:
            # それ以外のエラーを出力して終了
            print(f"エラー: {response.status_code} - {response.text}")
            return

    # 再試行がすべて失敗した場合
    print("すべての再試行が失敗しました。後でもう一度お試しください。")

if __name__ == "__main__":
    HF_TOKEN = "sk-BjPGEtjnOKHqyBwyj80xy0S3fU25lpBFxiSuOosYNdUf9myQ"  # Stability AI APIトークンを指定
    PROMPT = "Lighthouse on a cliff overlooking the ocean"  # 画像生成用のプロンプト

    # 画像生成関数を実行
    generate_image(prompt=PROMPT, token=HF_TOKEN)
