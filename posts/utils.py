# from diffusers import StableDiffusionPipeline
# # import torch
# import os
# import uuid

# # Stable Diffusionのパイプラインをロード（初回実行時にモデルがダウンロードされます）
# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-1", cache_dir="./model_cache")
# pipe = pipe.to("cuda")  # GPUがある場合

# def generate_ai_image(prompt_text):
#     # カンマをスペースに変換してプロンプトを生成
#     prompt = prompt_text.replace(',', ' ')
#     # 画像生成
#     image = pipe(prompt).images[0]
    
#     # 生成された画像を一時保存
#     image_path = f"generated_images/{uuid.uuid4()}.png"
#     os.makedirs("generated_images", exist_ok=True)
#     image.save(image_path)
    
#     return image_path  # 生成された画像のパスを返す