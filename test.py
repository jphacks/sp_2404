import requests
from PIL import Image
from io import BytesIO
import os
import time

def generate_image(prompt, token, output_path="output_image.png", retries=5, wait_time=120):
    """
    Generate an image using Hugging Face API from a text prompt.

    Args:
        prompt (str): The prompt to generate the image from.
        token (str): The Hugging Face API token.
        output_path (str): Path to save the generated image.
        retries (int): Number of retry attempts if the model is loading.
        wait_time (int): Wait time in seconds between retries.
    Returns:
        None
    """
    # api_url = "https://api-inference.huggingface.co/models/stable-diffusion-v1-5/stable-diffusion-v1-5"
    api_url = "https://api-inference.huggingface.co/models/Freepik/flux.1-lite-8B-alpha"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Retry loop for handling model loading status
    for attempt in range(retries):
        print(f"Sending request to Hugging Face API... (Attempt {attempt + 1}/{retries})")
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        
        if response.status_code == 200:
            print("Request successful. Loading image...")
            image = Image.open(BytesIO(response.content))
            image.save(output_path)
            print(f"Image saved to {output_path}")
            return
        elif response.status_code == 503 and attempt < retries - 1:
            print(f"Model is currently loading. Waiting for {wait_time} seconds before retrying...")
            time.sleep(wait_time)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break

if __name__ == "__main__":
    HF_TOKEN = "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"
    PROMPT = "A futuristic cityscape with flying cars and glowing skyscrapers"

    generate_image(prompt=PROMPT, token=HF_TOKEN)
