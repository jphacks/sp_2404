from diffusers import StableDiffusionPipeline

def download_model():
    # より軽量なStable Diffusion v1.1モデルをダウンロード
    pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-1", cache_dir="./model_cache")
    print("モデルのダウンロードが完了しました。")

if __name__ == "__main__":
    download_model()
